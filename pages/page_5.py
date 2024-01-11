# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

n = 0

# Titulo de Página
#st.title('Análise de dados: explorando dados de preço por barril do petróleo bruto tipo Brent (Ipeadata)')

st.set_page_config(layout="centered")

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Código para alinhar imagens expandidas no centro da tela e justificar textos
st.markdown(
    """
    <style>
        body {text-align: justify}
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

'''
## Modelo de previsões
'''
st.image(load_img('Imagens\ml.png'))
'''

Uma das etapas do nosso projeto foi a criação e treinamento de um modelo de previsões do preço do barril de petróleo utilizando Machine Learning.

Machine Learning é um processo de descoberta de padrões e extração de decisões de conjunto de dados desconhecidos.

Os modelos de Machine Learning podem ser treinados em grandes conjuntos de dados para executar tarefas, assim como em nosso projeto para a previsão do preço futuro do barril de pretóleo.

Para tal feito precisamos utilizar algorítmos adequados aos dados com os quais estamos trabalhando. Algoritmos são técnicas matemáticas utilizadas para encontrar padrões em conjuntos de dados. Para esse projeto, decidimos utilizar o algorítmo XGBRegressor (Extreme Gradient Boosting Regresso). 

O aumento de gradiente (Gradient boosting) refere-se a uma classe de algoritmos de aprendizado de máquina que podem ser usados para problemas de classificação ou modelagem preditiva de regressão. Aumento extremo de gradiente, ou XGB, para abreviar, é uma implementação eficiente de código aberto do algoritmo de aumento de gradiente. Como tal, o XGB é um algoritmo, um projeto de código aberto e uma biblioteca Python. Ele foi projetado para ser computacionalmente eficiente (rápido de executar) e altamente eficaz.
'''
st.divider()
'''
## Construção do modelo

A seguir, descreveremos as etapas utilizadas para a criação e treinamento do nosso modelo de previões:
'''
# Layout das etapas
tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Etapa 1",
                                              "Etapa 2",
                                              "Etapa 3",
                                              "Etapa 4",
                                              "Etapa 5",
                                              "Etapa 6"])

with tab0:
    '''
    ## Aquisição dos dados

    Inicialmente, utilizamos a biblioteca SQLAlchemy para fazer a interação com o banco de dados Postgres para recuperar os dados obtidos anteriormente através da técnica de webscraping.

    ```python
    # Imports necessário para o sqlalchemy nessa aplicação
    import pandas as pd
    from sqlalchemy.sql import text
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from decouple import Config, RepositoryEnv

    config = Config(RepositoryEnv(".env"))

    # Criação da engine e da sessão para acessar o banco de dados
    engine = create_engine(f"postgresql://{config('USER')}:{config('PASSWORD')}@{config('HOST')}:{config('PORT')}/tech")

    # Criando a sessão
    Sessao = sessionmaker(bind = engine)
    sessao = Sessao()

    # Lendo a tabela com o sqlalchemy
    sql = """ SELECT * FROM ptr.petro 
            ORDER BY petro.dt DESC"""

    query = sessao.execute(text(sql))

    resultado_query = query.all()

    sessao.close()
    ```
    '''
with tab1:
    '''
    ## Pré-processamento dos dados

    Após a interação com o banco de dados, iniciamos a preparação dos dados para a criação do nosso modelo de previsões. 

    Disponibilizamos a seguir o passo a passo do tratamento dos dados:

    1. Transformação do query em dataframe
    ```python
    # Transformando a query em dataframe
    df_query = pd.DataFrame(resultado_query, columns=['dt','preco'])
    ```

    2. Verificando as informações do DataFrame
    ```python
    # Verificando as informações do DataFrame
    df_query.info()
    ```
    ```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 11074 entries, 0 to 11073
    Data columns (total 2 columns):
    #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
    0   dt      11074 non-null  object
    1   preco   11074 non-null  object
    dtypes: object(2)
    memory usage: 173.2+ KB
    ```
    Pela resposta, podemos perceber que não há dados núlos em nosso dataframe. Também verificamos que tanto a coluna das data como a coluna dos preços estão com os respectivos datatypes incorretos.


    3. Convertendo coluna 'dt' para datetime
    ```python
    # Convertendo coluna 'dt' para datetime
    df_query['dt'] = pd.to_datetime(df_query['dt'], format='%Y-%m-%d')
    ```

    4. Convertendo valores da coluna 'preco' para tipo float
    ```python
    # Convertendo valores da coluna 'preco' para tipo float
    df_query['preco'] = df_query['preco'].str.replace(',', '.').astype(float)
    ```

    5. Verificando o shape do DataFrame
    ```python
    # verificando o shape do DataFrame
    df_query.shape
    ```
    ```
    (11074, 2)
    ```

    6. Verificando estatísticas da coluna preço
    ```python
    # Verificando estatísticas da coluna preco
    df_query['preco'].describe()
    ```
    ```
    count    11074.000000
    mean        52.754036
    std         33.240415
    min          9.100000
    25%         20.385000
    50%         47.805000
    75%         75.547500
    max        143.950000
    Name: preco, dtype: float64
    ```
    '''
with tab2:
    '''
    ## Criação e treino do modelo de previsão

    Aqui iniciamos a construção do nosso modelo de previsão utilizando o algorítmo XGBRegressor
    ```python
    # Importando libs de ML
    from sklearn.model_selection import train_test_split
    import xgboost as xgb

    # Criando uma cópia do DataFrame principal
    df_modelo = df_query.copy()
    df_modelo = df_modelo.sort_values(by='dt', ascending=True)

    # Criando as colunas de atraso (lag features)
    for lag in range(1, 4):
        df_modelo[f'preco_lag_{lag}'] = df_modelo['preco'].shift(lag)

    # Removendo valores nulos
    df_modelo = df_modelo.dropna()

    # Atribuindo os dados de treinamento
    X = df_modelo[['preco_lag_1','preco_lag_2','preco_lag_3']].values
    y = df_modelo['preco'].values

    # Criando uma seed de randomização
    SEED = 123

    # Separando os dados entre treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False, random_state=SEED)

    # Criando e treinando o modelo de XGBC
    model = xgb.XGBRegressor(n_estimators=100, max_depth=5, eta=0.1, seed=SEED)
    model.fit(X_train, y_train)

    # Fazendo previsões
    previsoes = model.predict(X_test)
    ```

    Em seguida, verificamos a erro absoluto médio e erro quadrado médio para validar a eficácia do nosso modelo 
    ```python
    # Importando libs de ML
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    # Avaliando modelo
    mse = mean_squared_error(y_test, previsoes)
    mae = mean_absolute_error(y_test, previsoes)

    # Imprimindo os valores de erro
    print("Mean Squared Error: ", mse)
    print("Mean Absolute Error: ", mae)
    ```
    ```
    Mean Squared Error:  3.1862769730266303
    Mean Absolute Error:  1.2110971996402093
    ```
    Pela resposta, temos que o erro absoluto médio e erro quadrado médio estão dentro do esperado. Assim, podemos prosseguir com a construção do modelo.
    '''
with tab3:
    '''
    ## Plotando os resultados
    '''
    st.image(load_img('Gráficos\original_vs_previsao.png'))
    '''
    ```python
    # Plotando resultados
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    plt.figure(figsize=(15,5))
    plt.plot(df_modelo['dt'].iloc[-len(y_test):], y_test, label='Original')
    plt.plot(df_modelo['dt'].iloc[-len(previsoes):], previsoes, label='Previsão')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()

    plt.legend()
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.grid(True)
    plt.title('Preços Originais vs Previsões (XGBC)')
    plt.show()
    ```
    '''
with tab4:
    '''
    ## Prevendo a próxima semana
    '''
    st.image(load_img('Gráficos\proxima_semana.png'))
    '''
    ```python
    # Prevendo a próxima semana
    previsoes_proxima_semana = previsoes[-7:]
    df_modelo_proxima_semana = df_modelo['dt'].iloc[-len(y_test):][-7:]

    plt.figure(figsize=(10,5))
    plt.plot(df_modelo_proxima_semana[::-1], previsoes_proxima_semana[::-1], label='Previsão', color='orange', marker='o')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()

    plt.title('Previsão dos Preços para a Próxima Semana')
    plt.xlabel('Data')
    plt.ylabel('Preço Previsto')
    plt.legend()
    plt.grid(True)
    plt.show()
    ```
    '''
with tab5:
    '''
    ## Armazenando o modelo
    ```python
    # Importando o Joblib para o salvamento do modelo
    import joblib

    # Salvando o modelo
    joblib.dump(model, 'Modelos\modelo_xgb.joblib')
    ```
    '''