# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

# Configurando a página
st.set_page_config(
    page_title="Tech-Challenge",
    page_icon="🛢️",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "Projeto criado para o *tech-challenge* do curso de pós-graduação da FIAP/Alura."
    }
)

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Titulo de Página
st.title('Análise de dados: explorando dados de preço por barril do petróleo bruto tipo Brent (Ipeadata)')

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

url = 'https://br.freepik.com/vetores-gratis/ilustracao-da-industria-de-petroleo-com-ilustracao-plana-de-extracao-de-petroleo_14662397.htm#query=petroleo&position=48&from_view=search&track=sph&uuid=3ddeddeb-5751-4d62-990d-750dfb9b75b5'
link = 'Imagem de macrovector'
st.image(load_img('Imagens/petro.jpg'))
st.markdown(f'[{link}]({url}) no Freepik')

'''
## Explorando dados de preço por barril do petróleo bruto tipo Brent (Ipeadata)


Links importantes:

[ipeadata.gov.br](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) - Preço por barril do petróleo bruto Brent (FOB) (IPEADATA)

[eia.doe.gov](https://www.eia.gov/dnav/pet/TblDefs/pet_pri_spt_tbldef2.asp) - U.S. Energy Information Administration (EIA), dados de consumo e produção global de petróleo

Links dos integrantes do projeto:

[github.com/GabrielPCO](https://github.com/GabrielPCO) - Github Gabriel Oliveira

[github.com/jackson-simionato](https://github.com/jackson-simionato) - Github Jackson Simionato

gabrielpcoliveira@gmail.com - Email Gabriel Oliveira

simionato.jackson@gmail.com - Email Jackson Simionato

haendelf@hotmail.com - Email Haendel Oliveira

'''
st.divider()
'''
## Resumo

O valor dos barris de petróleo tem preços diferentes de acordo com o tipo de extração. Em suma, existem dois métodos predominantes de extração do petróleo no mercado atual, sendo eles o Brent e WTI. Está análise será focada no preço do barril de petróleo do tipo Brent, com dados coletados a partir do site governamental Ipeadata, uma base de dados macroeconômicos, financeiros e regionais do Brasil mantida pelo Instituto de Pesquisa Econômica Aplicada.
Tais dados provém originalmente do órgão governamental norte-americano U.S. Energy Information Administration (EIA).

Produzido no Mar do Norte (Europa), Brent é uma classe de petróleo bruto que serve como benchmark para o preço internacional de diferentes tipos de petróleo. Neste caso, é valorado no chamado preço FOB (free on board), que não inclui despesa de frete e seguro no preço.

A seguir, será apresentado o plano de desenvolvimento de um modelo de previsão do preço do barril de petróleo Brent, utilizando os dados adquiridos do Ipeadata. Foram aplicados algoritmos de regressão em Machine Learning para a construção do modelo preditivo.

Além disso, foi realizada uma analise exploratória dos dados com relação as flutuações de preço observadas e dados de situações geopolíticas, crises econômicas e demanda global por energia. Esses fatores podem estar atrelados de alguma maneira as variações de preço encontradas nos dados brutos.

Finalmente, apresentamos ao leitor um dashboard resumindo toda a análise construida nessa pesquisa para um melhor entendimento do processo como um todo.
'''
st.divider()
'''
## Páginas

'''
col1, col2, col3, col4, col5, col6, col7 = st.columns([0.16,0.13,0.13,0.13,0.13,0.16,0.16])
with col1:
    if st.button('## Introdução', type='primary'):
        st.switch_page("_🛢️_Introdução.py")
with col2:
    if st.button('## Dataset'):
        st.switch_page("pages/2_📝_Dataset.py")
with col3:
    if st.button('## Projeto'):
        st.switch_page("pages/3_📋_Projeto.py")
with col4:
    if st.button('## Análise'):
        st.switch_page("pages/4_🔎_Análise.py")
with col5:
    if st.button('## Modelo'):
        st.switch_page("pages/5_📈_Modelo.py")
with col6:
    if st.button('## Dashboard'):
        st.switch_page("pages/6_📊_Dashboard.py")
with col7:
    if st.button('## Referências'):
        st.switch_page("pages/7_📑_Referências.py")
st.divider()
'''

## Observação

Os demais dados, DataFrames e outras análises mais aprofundadas podem ser encontradas na página de Github dos integrantes do grupo referenciadas no início desse documento.
'''