
import streamlit as st
from services.servico_sentimento import buscar_tweets_com_sentimento
from datetime import datetime, timedelta

st.set_page_config(page_title="Monitoramentos", page_icon=":mag:")
st.title("🕵️ Monitoramentos")

termo = st.text_input("Termo a Monitorar")
data_inicial = st.date_input("Data Inicial", value=datetime.now().date())
data_final = st.date_input("Data Final", value=datetime.now().date())
quantidade = st.slider("Quantidade de resultados", 1, 100, 10)

if st.button("Buscar Tweets"):
    if termo and data_inicial and data_final:
        try:
            data_inicio = datetime.combine(data_inicial, datetime.min.time())
            if data_final == datetime.now().date():
                data_fim = datetime.now() - timedelta(minutes=10)
            else:
                data_fim = datetime.combine(data_final, datetime.max.time())
            tweets = buscar_tweets_com_sentimento(termo, data_inicio, data_fim, quantidade)
            if tweets:
                for tweet in tweets:
                    st.write(tweet)
            else:
                st.info("Nenhum resultado encontrado para o termo informado.")
        except Exception as e:
            st.error(f"Erro na requisição: {str(e)}")
    else:
        st.warning("Por favor, preencha todos os campos.")
