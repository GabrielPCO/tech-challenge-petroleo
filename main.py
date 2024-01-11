# Bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Date, Float
from datetime import datetime
from decouple import Config, RepositoryEnv
import os.path
import sys

# Arquivo de configuração das informações sensíveis
config = Config(RepositoryEnv(".env"))


# Função Principal
def main():

    print("\n*********************")
    print("*Iniciando Programa.*")
    print("*********************")

    # Verifica a existência do arquivo ipeadata.csv
    print("\n-Verificando arquivo de base de dados")
    path = 'DataFrame\ipeadata.csv'
    check_file = os.path.isfile(path)

    # Cria o arquivo .csv caso o arquivo não for encontrado na pasta DataFrame
    if not check_file:
        ipeadata_df = pd.DataFrame(list())
        print("-Criando arquivo de base de dados")
        ipeadata_df.to_csv('DataFrame\ipeadata.csv')
    else:
        print("-Base de dados presente.") 
   
    # Lê o arquivo de armazenamento em .csv sem o index
    ipeadata_df = pd.read_csv("DataFrame\ipeadata.csv", index_col=0)  
    
    # Acessa o site do ipea para coletar os valores do preço do petróleo
    valores = acessar_ipea()

    # Verifica se há dados na variável valores
    if valores is None:
        return None

    # Cria o dataframe ipea
    ipea_df = criar_dataframe(valores)

    # Verifica se há dados no DataFrame ipea_df
    if ipea_df is None:
        return None

    # Se o arquivo .csv não estiver vazio ele irá verificar se o arquivo está sincronizado com os dados do IPEA
    if not ipeadata_df.empty:

        # Obtendo valor da data inicial da tabela do site do ipea
        data_inicial_site = ipea_df['dt']

        # Transforma a data da primeira linha em datatime
        data_inicial_arquivo = datetime.strptime(ipeadata_df['dt'][0], '%Y-%m-%d').date()

        # Verifica se os valores de data incial do site e do arquivo .csv são identicos
        if(data_inicial_site[0] == data_inicial_arquivo):
            print("\n-Arquivo e dados já estão atualizados.")
            return None

        # Cria um filtro para pegar apenas os novos valores
        filtro_df = ipea_df.loc[data_inicial_site > data_inicial_arquivo]

        if not filtro_df.empty:

            # Conecta e insere o DataFrame na tabela do database
            conexao = conectar_database()
            if conexao is None:
                print(f"[Erro ao adicionar linhas ao banco de dados.]")
                return None
            
            print(f"\n-Adicionando {filtro_df.shape[0]} linha(s) ao banco de dados.")
            filtro_df.to_sql('petro', conexao, schema="ptr", if_exists='append', index = False)
            print(f"[Linha(s) adicionadas com sucesso.]")

            # Concatena as novas informações
            concat_ipea_df = concatenar_arquivo(filtro_df,ipeadata_df)

            # Salva o DataFrame
            salvar_arquivo(concat_ipea_df)

    # Caso o arquivo .csv estiver vazio apenas sobe os dados para a tabela do database
    else:

        # Conecta e insere o DataFrame na tabela
        conexao = conectar_database()
        if conexao is None:
            return None
        ipea_df.to_sql('petro', conexao, schema="ptr", if_exists='replace', index = False)
        
        # Salva o DataFrame
        salvar_arquivo(ipea_df)

    # Atualiza o arquivo .csv
    conexao.commit()
    print("\n-Arquivo IPEA atualizado.")

    # Encerra o programa
    return conexao
    

# Acessa o site do ipea
def acessar_ipea():

    print("-Consultando site IPEA.")

    # Criando objeto URL
    url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'

    # Criando objeto pagina
    resposta = tentar_request(url)

    # Verifica a resposta do site
    if resposta is not None and resposta.status_code == 200:
        print("\n-Status da resposta do site: SUCESSO")
        pass
    else:
        print("\n-Status da resposta do site: FALHA")
        print("-Conexão não pode ser estabelecida.")
        return None

    print("\n-Iniciando coleta de dados.")
    print("Aguarde...")

    # parser-lxml = Alterando de html para um formato mais amigável ao Python
    # Obtendo informações da página
    soup = BeautifulSoup(resposta.text, 'lxml')

    # Obter informação da tag <table>
    tabela_01 = soup.find('table', id='grd_DXMainTable')

    # Obtem todos os valores das colunas com a tag <td>
    items = []
    for item in tabela_01.find_all('td'):
        titulo = item.text
        items.append(titulo)
    return items


# Cria o DataFrame IPEA
def criar_dataframe(val):

    print("\n-Iniciando criação do DataFrame IPEA.")
    print("Aguarde...")

    # Separando valores de nome de coluna
    colunas = ['dt','preco']
    
    # Separando valores de data
    datas = [val[6::2]]
    datas = achatar_lista(datas)

    # Separando valores de preço do petróleo
    preco = [val[7::2]]
    preco = achatar_lista(preco)

    if (len(datas) != len(preco)):
        print("\n-Status: ERRO!")
        print("-Local do Código: def main() if(ipeadata_df.empty)")
        print("-Erro de processamento: Quantidade de valores de 'data' e 'preço' incompatíveis.")
        return None

    dicionario = {colunas[0]: datas, colunas[1]: preco}
    df = pd.DataFrame(dicionario)

    # Transformando string da coluna data em datetime
    df['dt'] = pd.to_datetime(df['dt'], format='%d/%m/%Y').dt.date

    print("\n-DataFrame criado com sucesso.")

    return df


# Achata a lista para se tornar uma lista unidimensional
def achatar_lista(lista):
    return [x for linha in lista for x in linha]


# Tenta conectar ao site do IPEA
def tentar_request(url, num_tentativas=3, lista_sucesso=[200], **kwargs):
    for x in range(num_tentativas):
        try:
            resposta = requests.get(url, **kwargs)
            if resposta.status_code in lista_sucesso:
                return resposta
        except requests.exceptions.ConnectionError:
            print("\nStatus: ERRO!")
            print("Local do Código: def tentar_request()")
            print("Erro de processamento: Erro de conexção com o site")
            print(f"Tentativa: {x}")
    return None


# Conecta a database
def conectar_database():

    print("\n-Iniciando conexão com banco de dados")
    
    try:

        # Conectando a database
        print("Conectando...")

        engine = create_engine(f"postgresql://{config('USER')}:{config('PASSWORD')}@{config('HOST')}:{config('PORT')}/{config('DBNAME')}")
        conn = engine.connect()

        meta = MetaData(schema="ptr")

        students = Table('petro', meta, 
                         Column('dt', Date), 
                         Column('preco', Float)
                        )

        print("\n-Conexão com banco de dados: SUCESSO")

    except Exception as e:

        print("\nStatus: ERRO!")
        print("Local do Código: def conectar_database()")
        print("Erro de database: Erro de conexção com a database\n")
        print(e)

        return None
    
    # Criando a tabela petro se ela não existir na database
    print("\n-Atualizando tabela no banco de dados")
    print("Aguarde...")

    meta.create_all(engine, checkfirst=True)

    conn.commit()
    return conn


# Salva ou sobrescreve o arquivo de armazenamento .csv
def salvar_arquivo(df):

    # Gravando os dados obtidos por web scraping
    df.to_csv("DataFrame\ipeadata.csv")


# Concatena novos dados obtidos do site IPEA com os atuais
def concatenar_arquivo(df1,df2):

    # Concatenação dos DataFrames e correção do index
    concat_df = pd.concat([df1,df2])
    concat_df = concat_df.reset_index()
    concat_df = concat_df.drop(['index'], axis=1)
    return concat_df

# Encerra o programa
def encerrar_programa():

    print("\nEncerrando o programa...")
    sys.exit(0)


# Inicialização do script
if __name__ == '__main__':

    # Inicia a função main()
    connection = main()

    # verifica se há conexões pendentes
    if connection is not None:
        connection.close()

    # Encerra o programa
    encerrar_programa()