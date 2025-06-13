import streamlit as st
import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyD3omyfQGUY7HbRFiWUHoDPOypJvxG8njc"

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import base64
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# FOCO TOTAL NA INTERFACE E PRODUÇÂO STREAMLIT

# Example using a public URL (remains the same)

input_cafe = st.file_uploader("📸 Café da manhã", type=["jpg", "jpeg", "png"])
input_dinner = st.file_uploader("🍽️ Almoço", type=["jpg", "jpeg", "png"])
input_night = st.file_uploader("🌙 Janta", type=["jpg", "jpeg", "png"])


st.title("Semana saudavel com o modelo de IA Gemini 2.0")


def image_to_base64(file):
    if file is None:
        return None
    return base64.b64encode(file.read()).decode("utf-8")


if st.button("Pesquisar refeições"):
    for nome_refeicao, arquivo in {
        "Café da manhã": input_cafe,
        "Almoço": input_dinner,
        "Janta": input_night,
    }.items():
      if arquivo:
        img_base64 = image_to_base64(arquivo)
        message_local = HumanMessage(
            content=[
                {"type": "text", "text": "Descreva a imagem, colocando a quantidade de calorias sem falar que não sabe exatamente, e fale como um nutricionista com  a quantidade media de calorias"},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{img_base64}"},
            ]
        )
        result_local = llm.invoke([message_local])
        st.write(f"Marcus nutricionista resposta: {result_local.content}")
