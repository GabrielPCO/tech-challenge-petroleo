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

A seguir, os dados do preço do barril de petróleo serão analisados em relação à ocorrência de eventos políticos e socioeconômicos de grande relevância mundial, buscando correlacionar as variações de preço com as mudanças no contexto político global. 

Serão explorados temas como crises financeiras globais, guerras por petróleo, crises energéticas e variações na demanda e produção de energia que ocorreram a partir de 1987 (data inicial de nossos dados) até o período atual.

Esses eventos podem estar direta ou indiretamente ligados às variações de preço registradas no conjunto de dados, portanto é de grande valor verificar e analisar com mais minúcia para gerar possíveis insights com essas comparações.
'''
st.divider()
'''
## Análise geral - Power BI

'''

Dashboard_Power_BI = '<iframe title="tech_challenge_fase_4_pos_tech" style="width:100%; height:781px" src="https://app.powerbi.com/view?r=eyJrIjoiOTE3YTQ2MWQtNzc3MC00NTE3LThjOTgtYzM5YjY2ZjgyNjA2IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>' 

with st.container(height=790, border=False):
    st.markdown(Dashboard_Power_BI, unsafe_allow_html=True)

st.divider()

'''
Analisando o dashboard acima, é possível entender o contexto geral do mercado de petróleo, desde o início da série temporal até o período mais recente. Valores médios, mínimos e máximos são apresentados, seja com relação à toda série histórica ou apenas no recorte dos
últimos 12 meses. Além disso, o dashboard possui um histograma da distribuição do preço do barril de petróleo, bem como séries temporais de consumo e produção de petróleo e ocorrência de eventos políticos que podem ter impactado negativamente o mercado de petróleo.


Percebe-se que até o início da década de 2000, o preço do barril de petróleo nunca havia ultrapassado a marca de U$30 e havia uma certa estabilidade no mercado, com exceção do início da década de 1990, período em que a Guerra do Golfo foi travada na região do Kuwait.

Então, com a escalada das desavenças entre grupos como Al-Qaeda e países do Ocidente, principalmente os EUA, a partir da década de 2000 o preço do barril de petróleo começa a crescer em ritmo muito acelerado. Diversos eventos contribuíram para este contexto de volatilidade do mercado,
especialmente a Guerra do Iraque e a insegurança política do Oriente Médio como um todo. Em 2008, ocorre a primeira grande queda de preço (quase U$100 de queda), efeito direto da recessão econômica global originada por uma super bolha imobiliária e que levou à falência de diversos bancos importantes.

Os preços voltaram a subir no final de 2008 e chegaram ao patamar de U$110/BBL em maio de 2011. Três anos, de 2011 a 2014, de recorrentes altas e quedas foram observados, evidenciando o caráter muito mais volátil do mercado no século XXI, até que na metade de 2014 mais uma grande queda de preços ocorre.
Desta vez, a principal causa foi a redução na demanda por petróleo e o aumento da produção em países como EUA e Canadá, que passaram a extrair grandes quantidades de petróleo de xisto.

Após mais um período de altos e baixos entre 2016 e 2020, ocorre a pandemia da COVID-19 que impactou de maneira devastadora tanto a produção como o consumo de petróleo no mundo. O impacto foi tão grande que o barril de petróleo chegou a custar perto de U\$17. 
Com a volta do consumo após o fim da pandemia, o mercado se recuperou rapidamente atingindo a marca de 120 U\$/BBL, até que a partir de 2022 o mercado inicia uma nova fase de turbulência, marcada pela Guerra da Ucrânia e novos conflitos israelo-palestinos.

## Análise contextual

'''

# Layout das etapas
tab0, tab1, tab2 = st.tabs(["📊 Estatísticas",
                            "💸 Crise Financeira",
                            "🌎 Geopolítica"])
with tab0:
    '''
    ## Estatísticas dos dados

    Inicialmente, a função .describe() foi utilizada para avaliar as estatísticas básicas dos dados de preço do barril de petróleo em nosso dataset.
    ```python
    # Verificando estatísticas da coluna preco
    df_query['preco'].describe()
    ```
    ```
    count    11107.000000
    mean        52.836209
    std         33.225370
    min          9.100000
    25%         20.440000
    50%         47.950000
    75%         75.855000
    max        143.950000
    Name: preco, dtype: float64
    ```
    Atualmente, a série temporal é composta por 11107 registros de preço do barril de petróleo, uma quantidade razoável de dados para serem explorados.

    Além disso, a média de preço está em aproximadamente US\$52,84 com um desvio de US\$33,23. O preço máximo é de US\$143,95 e o mínimo de US\$9,10.
    '''
with tab1:
    '''
    ## Crises financeiras

    Nesta seção, as crises financeiras serão abordadas com mais detalhes para entender se há alguma correlação com os dados de preço do barril de petróleo.

    Os dados sobre as crises financeiras foram obtidos a partir do site investopedia.com (https://www.investopedia.com/articles/economics/08/past-recessions.asp)
    '''
    st.image(load_img('Gráficos/crise_financeira.png'))
    '''
    ### Análise

    Observa-se pelo gráfico que a maioria das principais recessões econômicas ocorridas no período aferido coincide com uma considerável variação no preço do barril de petróleo. Não significa que as recessões necessariamente causaram a grande volatilidade no preço do barril, mas pode indicar que esses dois fatores possuem alguma correlação entre si.
    
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

    Agora, será analisada a relação entre grandes conflitos armados e a variação dos preços de barril de petróleo ao longo do período abrangido pelo dataset.

    Por se tratar de um produto de grande valor para todos os países, diversos conflitos estão relacionados ao petróleo, sua extração, manipulação e comercialização, o que pode influenciar diretamente no comportamento da série temporal do preço do barril de petróleo.
    
    Os dados geopolíticos foram obtidos a partir da wikipédia (https://en.wikipedia.org/wiki/Oil_war)
    '''
    st.image(load_img('Gráficos/guerras.png'))
    '''
    ### Análise 

    Assim como na análise das crises financeiras, existe uma grande variação no preço do barril de petróleo que coincide com as guerras realizadas durante o período avaliado, portanto existe uma certa correlação das variações com os eventos bélicos. O petróleo é a principal fonte de renda de muitos países, sobretudo países do Oriente Médio. Ele é atualmente uma das principais fontes de energia e serve para a fabricação de variados produtos de alta utilidade.
    Dessa forma, por ser um item de extrema importância e muito disputado por diversos países do globo, é plausível que a variação do preço do barril de petróleo tenha uma correlação com guerras e outros conflitos armados.
    
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