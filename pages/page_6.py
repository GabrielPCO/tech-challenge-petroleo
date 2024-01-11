# Libs

import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb

# Libs gráficas

import plotly.graph_objects as go

# Streamlit

import streamlit as st

st.set_page_config(layout="wide")

@st.cache
def run_model():
    df_ipeadata = pd.read_csv("DataFrame/ipeadata.csv", index_col=0)
    df_ipeadata['preco'] = df_ipeadata['preco'].str.replace(',', '.').astype(float)

    df_modelo = pd.read_csv("DataFrame/df_modelo.csv", index_col=0)
    modelo = xgb.Booster()
    modelo.load_model('Modelos/modelo_xgb.json')

    # Atribuindo os dados de treinamento
    X = df_modelo[['preco_lag_1','preco_lag_2','preco_lag_3']].values
    y = df_modelo['preco'].values

    # Criando uma seed de randomização
    SEED = 123

    # Separando os dados entre treino e teste
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, shuffle=False, random_state=SEED)

    # Fazendo previsões
    previsoes = modelo.predict(X_test)

    return df_ipeadata, df_modelo, y_test, previsoes

df_ipeadata, df_modelo, y_test, previsoes = run_model()

'''
## Dashboard
'''

st.divider()

col1, col2 = st.columns([3,1])

with col1:

    col1_1, col1_2 = st.columns([1, 3])
    with col1_1:
        '''
        ### Barril de petroleo
        '''
        st.metric(label='Dados totais', value=df_ipeadata.shape[0])
        st.metric(label='Preço médio', value="US$"+str(format(df_ipeadata['preco'].mean().round(2), '.2f' )))
        st.metric(label='Preço máximo', value="US$"+str(format(df_ipeadata['preco'].max().round(2), '.2f' )))
        st.metric(label='Preço mínimo', value="US$"+str(format(df_ipeadata['preco'].min().round(2), '.2f' )))

    with col1_2:
        '''
        ### Modelo de previsão
        '''
        fig_1 = go.Figure()
        fig_1.add_trace(go.Scatter(x=df_modelo['dt'].iloc[-len(y_test):], y=y_test, line=dict(color="#070ab5"),  mode='lines', name='Original'))
        fig_1.add_trace(go.Scatter(x=df_modelo['dt'].iloc[-len(y_test):], y=previsoes, line=dict(color="#c97e04"), mode='lines', name='Previsão'))

        fig_1.update_layout(title='Preços Originais vs Previsões (XGBC)',
                        xaxis_title='Data',
                        yaxis_title='Preço')
        st.plotly_chart(fig_1,  use_container_width = True)

with col2:
    '''
    ### Prevendo os próximos dias
    '''

    option = st.selectbox(
        'Quantos dias você deseja para a previsão?',
        ('3 dias', '5 dias', '7 dias'))

    if option=='3 dias':
        # Prevendo a próxima semana
        previsoes_proxima_semana = previsoes[-3:]
        df_modelo_proxima_semana = df_modelo['dt'].iloc[-len(y_test):][-3:]
    elif option=='5 dias':
        # Prevendo a próxima semana
        previsoes_proxima_semana = previsoes[-5:]
        df_modelo_proxima_semana = df_modelo['dt'].iloc[-len(y_test):][-5:]
    elif option=='7 dias':
        # Prevendo a próxima semana
        previsoes_proxima_semana = previsoes[-7:]
        df_modelo_proxima_semana = df_modelo['dt'].iloc[-len(y_test):][-7:]


    fig_2 = go.Figure()
    fig_2.add_trace(go.Scatter(x=df_modelo_proxima_semana[::-1], y=previsoes_proxima_semana[::-1], line=dict(color="#c97e04"), mode='lines+markers', name='Previsão'))

    fig_2.update_layout(title='Previsão dos Preços para a Próxima Semana',
                    xaxis_title='Data',
                    yaxis_title='Preço Previsto')
    st.plotly_chart(fig_2,  use_container_width = True)