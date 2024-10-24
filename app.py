import streamlit as st
from transformers import pipeline

# Carregar pipeline de análise de sentimento
classifier = pipeline('sentiment-analysis')

# Configurar a página
st.set_page_config(
    page_title="Análise de Sentimento",
    page_icon="💬",
    layout="centered"
)

# Adicionar imagem na página inicial
st.image(
    "logo.jpg", 
    use_column_width=True
)

# Título da aplicação
st.title("🔍 Análise de Sentimento")

# Campo de entrada para o texto do usuário
user_input = st.text_area("Insira o texto para análise:")

# Função para analisar o texto usando o modelo pré-treinado
def analisar_sentimento(texto):
    resultado = classifier(texto)
    label = resultado[0]['label']
    
    # Retorna o resultado com emoji e a cor apropriada
    if label == "POSITIVE":
        return "Positivo 😊", "green"
    elif label == "NEGATIVE":
        return "Negativo 😡", "red"
    else:
        return "Neutro 😐", "yellow"

# Botão para iniciar a análise
if st.button("Analisar Sentimento"):
    if user_input:
        resultado, cor = analisar_sentimento(user_input)
        
        # Exibir o resultado com estilo e cor personalizada
        st.markdown(
            f"<h2 style='color: {cor}; text-align: center;'>O sentimento do texto é: {resultado}</h2>", 
            unsafe_allow_html=True
        )
    else:
        st.warning("Por favor, insira algum texto para analisar.")
