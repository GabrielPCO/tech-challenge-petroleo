# Libs

import pandas as pd

# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st
from st_pages import show_pages_from_config

show_pages_from_config()

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

# Titulo de Página
#st.title('Análise de dados: explorando dados de preço por barril do petróleo bruto tipo Brent (Ipeadata)')

st.set_page_config(layout="centered")

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
## DataFrame
'''
st.image(load_img('Imagens/dataframe.png'))
'''

Os dados dispostos a seguir foram coletados da base Ipeadata disponível no site do Ipea. Os dados estão apresentados em ordem decrescente desde a data da última atualização no site oficial.


'''
df = read_csv_file('DataFrame/ipeadata.csv')
df = df.drop(columns=df.columns[0], axis=1)
df = df.rename(columns={"dt":"Data","preco":"Preço do barril do petróleo bruto Brent (FOB) em US$ (Dólar americano)"})
df["Data"] = pd.to_datetime(df["Data"], format='%Y-%m-%d').dt.date
df["Preço do barril do petróleo bruto Brent (FOB) em US$ (Dólar americano)"] = df["Preço do barril do petróleo bruto Brent (FOB) em US$ (Dólar americano)"].str.replace(',', '.').astype(float)

# Convertendo o DataFrame em .csv
csv = convert_df(df)

st.dataframe(df)

# Botão de Download do DataFrame
st.download_button(
    label="Download do CSV",
    data=csv,
    file_name='ipeadata.csv',
    mime='text/csv',
)