import streamlit as st
from services.sentimento_service import classificar_sentimento

def painel_sentimento():
    st.header("Análise de Sentimento")
    texto = st.text_area("Digite um texto para analisar o sentimento:")
    if st.button("Analisar"):
        resultado = classificar_sentimento(texto)
        st.success(f"Sentimento detectado: {resultado}")
