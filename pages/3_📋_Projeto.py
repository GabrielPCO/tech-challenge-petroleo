# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Titulo de Página
#st.title('Análise de dados: explorando dados de preço por barril do petróleo bruto tipo Brent (Ipeadata)')

st.set_page_config(layout="centered",page_icon="🛢️")

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
## O Projeto

Nesta página, disponibilizamos um diagrama do projeto utilizado em nossa pesquisa. Nele, demonstramos todos os processos involvidos desde a captura dos dados até a construção da aplicação final com dashboard.

'''
st.image(load_img('Imagens/Projeto.png'), caption='Diagrama do projeto')
st.divider()
'''
## Detalhamento do projeto

A seguir, detalhamos cada etapa exibida no diagrama para um melhor entendimento sobre o processo como um todo:
'''

# Layout das etapas
tab0, tab1, tab2, tab3, tab4 = st.tabs(["Etapa 1",
                                        "Etapa 2",
                                        "Etapa 3",
                                        "Etapa 4",
                                        "Etapa 5"])

with tab0:
    '''
    ## Captura dos dados
    '''
    st.image(load_img('Imagens/webscraping.png'))
    '''

    Como mencionado anteriormente, utilizamos para nossa pesquisa a base de dados Ipeadata disponibilizada no site do Ipea. Como os dados do preço do barril de petróleo são atualizados constantemente de semana a semana, decidimos por criar um scrip em python para a captura dos dados.

    Esse script realiza semanalmente a raspagem dos dados disponibilizado no site, coletando-os a partir de uma grande tabela que contém o histórico de preço do barril de petróleo desde o ano de 1987 até os dias atuais.

    Esses dados são, então, tratados e armazenados em um banco de dados Postgres e em um arquivo .csv para posterior conferência.
    '''
with tab1:
    '''
    ## Pré-processamento e análise
    '''
    st.image(load_img('Imagens/processamento_analise.png'))
    '''

    Os dados coletados são pré-processados para a posterior análise e também para a criação do nosso modelo de previsões do preço do barril de petróleo. O pré-processamento é uma etapa fundamental para a preparação, organização e estruturação dos dados, assim garantimos que não chegaremos a falsas conclusões e previsões por conta de valores faltantes, outliers, etc.

    Em seguida, os dados são analisados em relação a diversos fatores que podem influenciar direta ou indiretamente a variação do preço do barril de petróleo. Fatores como situações geopolíticas, crises econômicas e demanda global por energia.
    '''
with tab2:
    '''
    ## Modelo em Machine Learning
    '''
    st.image(load_img('Imagens/ml.png'))
    '''

    A próxima etapa é criar um modelo em Machine Learning para a previsão do preço do barril de petróleo. O modelo é alimentado com os nossos dados pré-processados e, então, utilizamos o algoritmo XGBRegressor (Extreme Gradient Boosting Regressor) para o seu treinamento.

    Finalmente, salvamos o modelo em um arquivo .joblib para o posterior uso na construção dos dashboards em Power BI e streamlit.
    '''
with tab3:
    '''
    ## Dashboard
    '''
    st.image(load_img('Imagens/dashboard.png'))
    '''

    Para o dashboard, decidimos utilizar duas abordagens. Inicialmente, utilizamos o Power BI para sua construção. Power BI é uma plataforma unificada e escalonável para autoatendimento e BI (business intelligence). De maneira geral, o Power BI é utilizado para a construção de relatórios e painéis (dashboards). Eles reúnem informações visuais e dinâmicas acerca de conjuntos de dados (datasets), e também trabalham com o processo de entrega desses resultados através de plataformas, como a própria web.

    Também utilizamos Streamlit para a construçã do dashboard. O Streamlit é um framework desenvolvido em Python que torna possível a criação de aplicativos elegantes para modelos de machine learning (aprendizagem de máquina) ou mesmo visualização de dados para uma simples análise exploratória de um dataset (conjunto de dados), o que o torna ideal para o nosso projeto.
    '''
with tab4:
    '''
    ## Conclusão

    Com todos esses processos funcionando em conjunto temos um produto de grande valor agregado em mãos. Agora, as informações do preço do barril de petróleo estão dispostas de forma clara, susinta, organizada e atualizada, gerando um maior conforto, agilidade e produtividade para o usuário final.
    '''