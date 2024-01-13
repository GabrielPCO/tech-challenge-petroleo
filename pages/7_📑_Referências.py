# Streamlit

import streamlit as st

st.set_page_config(layout="centered",page_icon="🛢️")

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
## Referências

1. GOMES, Pedro César Tebaldi. Conheça as Etapas do Pré-Processamento de dados. DATAGEEKS, 20019. Disponível em: https://www.datageeks.com.br/pre-processamento-de-dados/. Acessado em: 10, janeiro de 2024.

2. BROWNLEE, Jason. XGBoost for Regression. Machine Learning Mastery, 2021. Disponível em: https://machinelearningmastery.com/xgboost-for-regression/. Acessado em: 10, janeiro de 2024.

3. GOBBO, Debora. Desenvolvimento de um aplicativo Web utilizando Python e Streamlit. DATA HACKERS, 2021. Disponível em: https://medium.com/data-hackers/desenvolvimento-de-um-aplicativo-web-utilizando-python-e-streamlit-b929888456a5. Acessado em: 10, janeiro de 2024.

4. Modelos de machine learning. Databricks, 2023. Disponível em: https://www.databricks.com/br/glossary/machine-learning-models. Acessado em: 10, janeiro de 2024.

5. US Recessions Throughout History: Causes and Effects. Ivestopedia, 2023. Disponível em: https://www.investopedia.com/articles/economics/08/past-recessions.asp. Acessado em: 10, janeiro de 2024.

6. Oil war. In: WIKIPÉDIA: a enciclopédia livre. [São Francisco, CA: Fundação Wikimedia], 2024. Disponível em: https://en.wikipedia.org/wiki/Oil_war. Acessado em: 10, janeiro de 2024.

7. MAKHIJANI, Charu. Machine Learning Model Deployment as a Web App using Streamlit. Medium, 2023. Disponível em: https://charumakhijani.medium.com/machine-learning-model-deployment-as-a-web-app-using-streamlit-4e542d0adf15. Acessado em: 10, janeiro de 2024.

8. PŁOŃSKI, Piotr. How to save and load Xgboost in Python?. Mljar, 2021. Disponível em: https://mljar.com/blog/xgboost-save-load-python/. Acessado em: 10, janeiro de 2024.
'''