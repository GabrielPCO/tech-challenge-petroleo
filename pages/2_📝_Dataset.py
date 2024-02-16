# Libs

import pandas as pd

# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

# Função para a leitura da base de dados
@st.cache_data
def read_csv_file(file):
    return pd.read_csv(file)

# Função do botão de Download para converter o DataFrame em .csv
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

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
## Dataset
'''
st.image(load_img('Imagens/dataframe.png'))
'''

Os dados dispostos a seguir são originalmente produzidos pelo U.S. Energy Information Administration (EIA) e disponibilizados pelo Ipea no portal Ipeadata. Os dados estão apresentados em uma tabela .csv em ordem decrescente desde a data da última atualização no site oficial.

[Ipea](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) - Preço por barril do petróleo bruto Brent (FOB) (Ipeadata)

[EIA](https://www.eia.gov/dnav/pet/hist/rbrteD.htm) - Preço por barril do petróleo bruto Brent (FOB) (EIA)

'''
df = read_csv_file('DataFrame/ipeadata.csv')
df = df.drop(columns=df.columns[0], axis=1)
df = df.rename(columns={"dt":"Data","preco":"Preço do barril do petróleo bruto Brent (FOB) em US$ (Dólar americano)"})
df["Data"] = pd.to_datetime(df["Data"], format='%Y-%m-%d').dt.date
df["Preço do barril do petróleo bruto Brent (FOB) em US$ (Dólar americano)"] = df["Preço do barril do petróleo bruto Brent (FOB) em US$ (Dólar americano)"].str.replace(',', '.').astype(float)

# Convertendo o DataFrame em .csv
csv = convert_df(df)

st.markdown(':gray[*Atualizado em 16/02/2024*]')

st.dataframe(df)

# Botão de Download do DataFrame
st.download_button(
    label="Download do CSV",
    data=csv,
    file_name='ipeadata.csv',
    mime='text/csv',
)