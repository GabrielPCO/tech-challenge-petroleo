# Libs

import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb

# Libs gráficas

import plotly.graph_objects as go

# Streamlit

import streamlit as st

st.set_page_config(layout="wide",page_icon="🛢️")

esconder_expande = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(esconder_expande, unsafe_allow_html=True)

df_ipeadata = pd.read_csv("DataFrame/ipeadata.csv", index_col=0)
df_ipeadata['dt'] = pd.to_datetime(df_ipeadata['dt'], format='%Y-%m-%d').dt.date
df_ipeadata['preco'] = df_ipeadata['preco'].str.replace(',', '.').astype(float)

df_modelo = pd.read_csv("DataFrame/df_modelo.csv", index_col=0)

modelo = xgb.XGBRegressor()
modelo.load_model("Modelos/modelo_xgb.json")

# Atribuindo os dados de treinamento
X = df_modelo[['preco_lag_1','preco_lag_2','preco_lag_3']].values
y = df_modelo['preco'].values

# Criando uma seed de randomização
SEED = 123

# Separando os dados entre treino e teste
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, shuffle=False, random_state=SEED)

# Fazendo previsões
previsoes = modelo.predict(X_test)

# Cores Dashboard
color_1 = '#3972ED' # azul claro
color_2 = '#2B2BB4' # azul escuro
color_3 = '#e88b10' # laranja
color_4 = '#449540' # verde
color_5 = '#1C1C1B' # preto (fundo)

col1, col2 = st.columns([0.6,0.4])

with col1:
    '''
    ## Modelo de previsão
    '''
    fig_1 = go.Figure()
    fig_1.add_trace(go.Scatter(x=df_modelo['dt'].iloc[-len(y_test):], y=y_test, line=dict(color=color_2),  mode='lines', name='Original'))
    fig_1.add_trace(go.Scatter(x=df_modelo['dt'].iloc[-len(y_test):], y=previsoes, line=dict(color=color_3), mode='lines', name='Previsão'))

    fig_1.update_layout(title='Preços Originais vs Previsões (XGBC)',
                    yaxis_title='Preço',
                    yaxis = dict(fixedrange = False))

    st.plotly_chart(fig_1,  use_container_width = True)

with col2:

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
    fig_2.add_trace(go.Scatter(x=df_modelo_proxima_semana[::-1], y=previsoes_proxima_semana[::-1], line=dict(color=color_3), mode='lines+markers', name='Previsão'))

    fig_2.update_layout(title='Previsão dos Preços para a Próxima Semana',
                    xaxis_title=f"{df_ipeadata['dt'][0].year}",
                    yaxis_title='Preço Previsto')
    
    fig_2.update_xaxes(
        dtick="D1", # sets minimal interval to day
        tickformat="%d %b<br>(%a)", # the date format you want 
    )

    st.plotly_chart(fig_2,  use_container_width = True)

col3, col4, col5 = st.columns([0.3,0.2,0.5])

with col3:

    with st.container(border=True):
        col3_1, col3_2 = st.columns(2)
        with col3_1:
            '''
            ### Barril de petroleo
            '''
            st.metric(label='Dados totais', value=df_ipeadata.shape[0])
            num_01 = df_ipeadata['preco'].values[0]
            num_02 = df_ipeadata['preco'].values[1]
            st.metric(label='Último preço', value="US$"+str(format(df_ipeadata['preco'].values[0].round(2), '.2f' )).replace('.',','), delta=str(format((((num_01-num_02)/((num_01+num_02)/2))*100).round(2), '.2f')).replace('.',',')+'%')
        with col3_2: 
            st.metric(label='Preço médio', value="US$"+str(format(df_ipeadata['preco'].mean().round(2), '.2f' )).replace('.',','))
            st.metric(label='Preço máximo', value="US$"+str(format(df_ipeadata['preco'].max().round(2), '.2f' )).replace('.',','))
            st.metric(label='Preço mínimo', value="US$"+str(format(df_ipeadata['preco'].min().round(2), '.2f' )).replace('.',','))

with col4:
    st.markdown("<h3 style='text-align: center;'>Acurácia do modelo</h3>", unsafe_allow_html=True)

    accuracy = float(format(modelo.score(X_test, y_test)*100, '.2f'))

    df_accuracy = pd.DataFrame({'names' : ['Acurácia',' '],
                   'values' :  [accuracy, 100 - accuracy]})
    
    fig_3 = go.Figure()
    
    fig_3.add_trace(go.Pie(labels=df_accuracy['names'], values=df_accuracy['values'], name="Acurácia"))
    
    colors = [color_4, color_5]

    fig_3.update_traces(hole=0.7, hoverinfo='none',  marker=dict(colors=colors), showlegend=False, textinfo='none')

    fig_3.update_layout(margin=dict(t=0, b=0, l=0, r=0),autosize=False, width=200, height=200,
                        annotations=[dict(text=str(df_accuracy['values'][0]).replace('.',',')+'%', x=0.5, y=0.5, font_size=20, showarrow=False)])

    st.plotly_chart(fig_3,  use_container_width = True)

with col5:
    '''
    ### Distribuição de frequência dos preços
    '''

    fig_4 = go.Figure(data=[go.Histogram(x=df_ipeadata['preco'])])

    marker_color = []
    for x in range(0,80):
        if x == 5:
            marker_color.append(color_2)
        else:
            marker_color.append(color_1)

    fig_4.update_traces(marker_color=marker_color)

    fig_4.update_layout(margin=dict(t=0, b=0, l=0, r=0),autosize=False, width=200, height=200)

    st.plotly_chart(fig_4,  use_container_width = True)

st.divider()

'''
## Power BI

'''

Dashboard_Power_BI = '<iframe title="tech_challenge_fase_4_pos_tech" style="width:100%; height:100vh" src="https://app.powerbi.com/view?r=eyJrIjoiOTE3YTQ2MWQtNzc3MC00NTE3LThjOTgtYzM5YjY2ZjgyNjA2IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>' 

st.markdown(Dashboard_Power_BI, unsafe_allow_html=True)