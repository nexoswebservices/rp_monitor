
def analisar_sentimento_usuario(texto, tipo_usuario="free"):
    if tipo_usuario == "pro":
        try:
            from services.sentimento_service import analisar_sentimento as openai_analise
            return openai_analise(texto)
        except Exception as e:
            return {"label": "Erro", "score": 0.0, "erro": str(e)}
    else:
        try:
            from analisador_sentimento import analisar_sentimento as hf_analise
            return hf_analise(texto)
        except Exception as e:
            return {"label": "Erro", "score": 0.0, "erro": str(e)}
