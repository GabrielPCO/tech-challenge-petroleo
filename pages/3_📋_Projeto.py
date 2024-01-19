# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

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
## O projeto

A seguir, é ilustrado um diagrama de execução do Tech Challenge. Nele, são demonstradas todas as etapas e processamentos envolvidos, desde a aquisição dos dados até a construção da aplicação final com dashboard.

'''
st.image(load_img('Imagens/Projeto.png'), caption='Diagrama do projeto')
st.divider()
'''
## Etapas do projeto

Nesta seção, as etapas do diagrama serão detalhadas para um melhor entendimento do método aplicado no projeto:
'''

# Layout das etapas
tab0, tab1, tab2, tab3, tab4 = st.tabs(["Aquisição dos dados",
                                        "Pré-processamento e análise",
                                        "Modelo de Machine Learning",
                                        "Dashboard",
                                        "Conclusão"])

with tab0:
    '''
    ## Aquisição dos dados
    '''
    st.image(load_img('Imagens/webscraping.png'))
    '''

    Como mencionado anteriormente, neste projeto foi utilizada a base de dados Ipeadata disponibilizada no site do Ipea. Como os dados do preço do barril de petróleo são atualizados constantemente de semana a semana, um script em python foi criada para realizar a aquisição recorrente dos dados mais atualizados.

    Esse script realiza semanalmente a raspagem dos dados disponibilizado no site, coletando-os a partir de uma grande tabela que contém o histórico de preço do barril de petróleo desde o ano de 1987 até o presente.

    Depois, esta base de dados é tratada e armazenada em um banco de dados Postgres e em um arquivo .csv para posterior conferência.
    '''
with tab1:
    '''
    ## Pré-processamento e análise
    '''
    st.image(load_img('Imagens/processamento_analise.png'))
    '''

    Após a aquisição, os dados foram pré-processados para a posterior análise e também para a criação do modelo que busca prever o preço do barril de petróleo. O pré-processamento é uma etapa fundamental para a preparação, organização e estruturação dos dados, assim há maior confiabilidade nas previsões e conclusões do modelo, considerando ocorrência de valores faltantes, outliers, etc.

    Em seguida, foi realizada uma análise exploratória dos dados com relação a diversos fatores que podem influenciar direta ou indiretamente a variação do preço do barril de petróleo. Fatores como situações geopolíticas, crises econômicas e demanda global por energia foram analisados. Nesta etapa, foi realizado o cálculo de medidas descritivas, a plotagem de gráficos e a construção de um dashboard em PowerBI.
    '''
with tab2:
    '''
    ## Modelo de Machine Learning
    '''
    st.image(load_img('Imagens/ml.png'))
    '''

    A etapa seguinte consistiu na criação de um modelo de Machine Learning para a previsão do preço do barril de petróleo. O modelo os dados pré-processados na etapa anterior e, então, o algoritmo XGBRegressor (Extreme Gradient Boosting Regressor) é aplicada no treinamento.

    Por fim, o modelo foi salvo em um arquivo .json para o posterior uso na construção dos dashboards em Power BI e streamlit.
    '''
with tab3:
    '''
    ## Dashboard
    '''
    st.image(load_img('Imagens/dashboard.png'))
    '''

    Um segundo dashboard foi construído utilizando as próprias ferramentas do Streamlit, com o objetivo de apresentar os resultados do modelo de Machine Learning de maneira simples e eficaz. O Streamlit é um framework desenvolvido em Python que torna possível a criação de aplicativos elegantes para modelos de machine learning (aprendizagem de máquina) ou mesmo visualização de dados para uma simples análise exploratória de um dataset (conjunto de dados), o que o torna ideal para o presente projeto.
    '''
with tab4:
    '''
    ## Conclusão

    Com todos esses processos funcionando em conjunto, tem-se um produto de grande valor agregado. Agora, as informações do preço do barril de petróleo estão dispostas de forma clara, sucinta, organizada e atualizada, gerando um maior conforto, agilidade e produtividade para o usuário final.
    '''