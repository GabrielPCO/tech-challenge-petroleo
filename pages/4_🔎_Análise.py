# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

st.set_page_config(layout="centered",page_icon="🛢️")

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

# Alterando cor dos hyperlinks
st.markdown(
   """
    <style>
     a:link {
       color: #F63366;
       background-color: transparent;
       text-decoration: none;
     }

     a:visited {
        color: #98072d;
        background-color: transparent;
        text-decoration: none;
    }

     a:hover {
        color: #F63366;
        background-color: transparent;
        text-decoration: none;
    }

    a:active {
        color: #F63366;
        background-color: transparent;
        text-decoration: none;
    }
    </style>
    """ , unsafe_allow_html=True
)

'''
## Análise exploratória
'''
st.image(load_img('Imagens/processamento_analise.png'))
'''

A seguir, iremos analisar os dados do preço do barril de petróleo em relação a diversas situações que ocorreram durante o período de tempo tratado em noso dataset. 

Iremos explorar temas como grandes crises financeiras globais, guerras por petróleo e as diversas crises energéticas que eclodiram a partir dos anos de 1987 (data inicial de nossos dados) até o período atual.

Esses eventos podem estar direta ou indiretamente ligados as variações de preço que encontramos ao longo dos nossos dados. Assim, seria interessante verificar e analisar com mais minúcia para gerar possíveis insights com essas comparações.
'''
st.divider()
'''
## Análise geral - Power BI

'''

Dashboard_Power_BI = '<iframe title="tech_challenge_fase_4_pos_tech" style="width:100%; height:81vh" src="https://app.powerbi.com/view?r=eyJrIjoiOTE3YTQ2MWQtNzc3MC00NTE3LThjOTgtYzM5YjY2ZjgyNjA2IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>' 

with st.container(height=790, border=False):
    st.markdown(Dashboard_Power_BI, unsafe_allow_html=True)

st.divider()

'''
## Análise contextual

'''

# Layout das etapas
tab0, tab1, tab2 = st.tabs(["📊 Estatísticas",
                            "💸 Crise Financeira",
                            "🌎 Geopolítica"])
with tab0:
    '''
    ## Estatísticas dos dados

    Inicialmente, utilizamos o método .describe() para avaliar as estatísticas básicas dos dados de preço do barril de petróleo em nosso dataset.
    ```python
    # Verificando estatísticas da coluna preco
    df_query['preco'].describe()
    ```
    ```
    count    11082.000000
    mean        52.771962
    std         33.235140
    min          9.100000
    25%         20.400000
    50%         47.845000
    75%         75.667500
    max        143.950000
    Name: preco, dtype: float64
    ```
    Podemos perceber algumas informações importantes. Temos atualmente 11074 valores de preço do barril de petróleo, uma quantidade razoável de dados para serem explorados.

    Além disso, a média de preço está em aproximadamente US\$52,77 com um desvio de US\$33,23. O preço máximo é de US\$143,95 e o mínimo de US\$9,10.
    '''
with tab1:
    '''
    ## Crises financeiras

    Aqui, estudaremos um pouco das crises financeiras que podem estar ligadas ou terem alguma correlação com os nossos dados de preço do barril de petróleo.

    Os dados sobre as crises financeiras foram obtidos a partir do site investopedia.com (https://www.investopedia.com/articles/economics/08/past-recessions.asp)
    '''
    st.image(load_img('Gráficos/crise_financeira.png'))
    '''
    ### Análise

    Podemos verificar pelo gráfico que a maioria das principais recessões econômicas que tivemos no período aferido coincide com uma consideravel variação no preço do barril de petróleo. Não significa que as recessões necessariamente causaram a grande volatilidade no preço do barril, mas pode indicar que esses dois fatores possuem alguma correlação entre si.
    
    ```python
    fig, ax = plt.subplots(1, figsize=[14,4])
    ax.plot(df_ipeadata['dt'], df_ipeadata['preco'])

    for x in range(0, df_crise_financeira.shape[0]):
        inicio = df_crise_financeira['Início'][x].to_timestamp().date()
        termino = df_crise_financeira['Término'][x].to_timestamp().date()
        ax.axvspan(inicio, termino, facecolor='gray', edgecolor='none', alpha=.5)
        if x==2:
            ax.text(inicio + pd.Timedelta(days=80), df_ipeadata['preco'].values.max()/3, df_crise_financeira['Evento'][x], rotation=90, va='center', fontsize=8)
        else:
            ax.text(inicio + pd.Timedelta(days=80), df_ipeadata['preco'].values.max()/1.5, df_crise_financeira['Evento'][x], rotation=90, va='center', fontsize=8)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()

    plt.title('Principais crises financeiras vs preço do barril de petróleo (EPCBRENT, 1987-2023)')
    plt.ylabel('Preço do barril de petróleo (US$/BBL)')
    plt.grid(True)
    plt.show()
    ```
    '''
with tab2:
    '''
    ## Principais conflitos geopolíticos relacionados ao petróleo

    Analisaremos agora a relação de conflitos bélicos e a variação dos preços de barril de petróleo ao longo do período aferido em nosso dataset.

    Por se tratar de um produto de alta utilidade para diversos países, acreditamos que conflitos relacionados ao petróleo, sua extração, manipulação e comercialização podem influenciar nas variações observadas de preço.
    
    Os dados geopolíticos foram obtidos a partir da wikipédia (https://en.wikipedia.org/wiki/Oil_war)
    '''
    st.image(load_img('Gráficos/guerras.png'))
    '''
    ### Análise 

    Podemos perceber que assim como na análise das crises financeiras, existe uma grande variação no preço do barril de petróleo que coincide com as guerras realizadas durante o perído avaliado. Notamos que existe uma certa correlação das variações com os eventos bélicos. O petróleo é a principal fonte de renda de muitos países, sobretudo o Oriente Médio. Ele é atualmente uma das pricipais fontes de energia e serve para a fabricação de variados produtos de alta utilidade. Dessa forma, podemos inferir que o petróleo é um ítem de extrema importancia e muito disputado por diversos países do globo. Assim, é plausível que a variaçã do preço do barril de petróleo tenha uma correlação com eventos de cunho bélico como observado pela comparação destacada no gráfico.
    
    ```python
    fig, ax = plt.subplots(1, figsize=[14,4])
    ax.plot(df_ipeadata['dt'], df_ipeadata['preco'])

    for x in range(0, df_guerra_petroleo.shape[0]):
        if x==0:
            inicio = df_ipeadata['dt'].min()
        else:
            inicio = df_guerra_petroleo['Início'][x].to_timestamp().date()
        termino = df_guerra_petroleo['Término'][x].to_timestamp().date()

        if x==3:
            ax.axvspan(inicio + pd.Timedelta(days=100), termino, facecolor='gray', edgecolor='none', alpha=.5)
        else:
            ax.axvspan(inicio, termino, facecolor='gray', edgecolor='none', alpha=.5)

        if x==4:
            ax.text(inicio + pd.Timedelta(days=80), df_ipeadata['preco'].values.max()/3, df_guerra_petroleo['Evento'][x], rotation=90, va='center', fontsize=8)
        elif x==3:
            ax.text(inicio + pd.Timedelta(days=1000), df_ipeadata['preco'].values.max()/2.5, df_guerra_petroleo['Evento'][x], rotation=90, va='center', fontsize=8)
        elif x==2:
            ax.text(inicio + pd.Timedelta(days=1400), df_ipeadata['preco'].values.max()/1.3, df_guerra_petroleo['Evento'][x], rotation=90, va='center', fontsize=8)
        else:
            ax.text(inicio + pd.Timedelta(days=80), df_ipeadata['preco'].values.max()/2.5, df_guerra_petroleo['Evento'][x], rotation=90, va='center', fontsize=8)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()

    plt.title('Principais guerras vs preço do barril de petróleo (EPCBRENT, 1987-2023)')
    plt.ylabel('Preço do barril de petróleo (US$/BBL)')
    plt.grid(True)
    plt.show()
    ```
    '''