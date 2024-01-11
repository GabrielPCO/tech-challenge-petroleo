# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st
from st_pages import Page, show_pages

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

show_pages(
    [
        Page("https://tech-challenge-petroleo-obfkqnzeymbcecjew3rxlb.streamlit.app", "Introdução", "🛢️"),
        Page("https://tech-challenge-petroleo-obfkqnzeymbcecjew3rxlb.streamlit.app/page_2", "DataFrame", "📝"),
        Page("https://tech-challenge-petroleo-obfkqnzeymbcecjew3rxlb.streamlit.app/page_3", "Projeto", "📋"),
        Page("https://tech-challenge-petroleo-obfkqnzeymbcecjew3rxlb.streamlit.app/page_4", "Análise", "🔎"),
        Page("https://tech-challenge-petroleo-obfkqnzeymbcecjew3rxlb.streamlit.app/page_5", "Modelo", "📈"),
        Page("https://tech-challenge-petroleo-obfkqnzeymbcecjew3rxlb.streamlit.app/page_6", "Dashboard", "📊"),
        Page("https://tech-challenge-petroleo-obfkqnzeymbcecjew3rxlb.streamlit.app/page_7", "Referências", "📑"),
    ]
)

url = 'https://br.freepik.com/vetores-gratis/ilustracao-da-industria-de-petroleo-com-ilustracao-plana-de-extracao-de-petroleo_14662397.htm#query=petroleo&position=48&from_view=search&track=sph&uuid=3ddeddeb-5751-4d62-990d-750dfb9b75b5'
link = 'Imagem de macrovector'
st.image(load_img('Imagens/petro.jpg'))
st.markdown(f'[{link}]({url}) no Freepik')

'''
## Explorando dados de preço por barril do petróleo bruto tipo Brent (Ipeadata)


Links importantes:

[ipeadata.gov.br](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) - Preço por barril do petróleo bruto Brent (FOB) (IPEADATA)

[eia.doe.gov](https://www.eia.gov/dnav/pet/TblDefs/pet_pri_spt_tbldef2.asp) - Energy Information Administratio (EIA)

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

O valor dos barris de petróleo tem preços diferentes de acordo com o tipo de extração. Em suma, existem dois métodos predominantes de extração do petróleo no mercado atual, sendo eles o Brent e WTI. Nossa análise focará no preço do barril de petróleo do tipo Brent com dados coletados a partir do site governamental Ipeadata, uma base de dados macroeconômicos, financeiros e regionais do Brasil mantida pelo Ipea.

Produzido no Mar do Norte (Europa), Brent é uma classe de petróleo bruto que serve como benchmark para o preço internacional de diferentes tipos de petróleo. Neste caso, é valorado no chamado preço FOB (free on board), que não inclui despesa de frete e seguro no preço.

A seguir, demonstramos um plano de desenvolvimento e produção de um modelo de previsões do preço do barril de petróleo do tipo Brent com os dados adquiridos do Ipeadata. Utilizamos algoritmos de regressão em Machine Learning para a construção do modelo de previsões.

Além disso, realizamos uma analise exploratória em relação as flutuações de preço observadas e dados de situações geopolíticas, crises econômicas e demanda global por energia. Esses fatores podem estar atrelados de alguma maneira as variações de preço encontradas nos dados brutos.

Finalmente, apresentamos ao leitor um dashboard resumindo toda a análise construida nessa pesquisa para um melhor entendimento do processo como um todo.
'''
st.divider()
'''

## Observação

Os demais dados, DataFrames e outras análises mais aprofundadas podem ser encontradas na página de Github dos integrantes do grupo referenciadas no início desse documento.
'''