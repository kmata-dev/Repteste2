import streamlit as st
import time # Vamos usar para um efeitinho de suspense

# --- Configuração da Página ---
st.set_page_config(page_title="Meu Questionário Turbinado", layout="centered")

# --- Início do App ---
st.title("E aí, beleza? Bora bater um papo!")
st.write("Me responde umas coisinhas aqui. Prometo que sou um robô legal.")

# --- Perguntas ---

# Pergunta 1: Nome
nome = st.text_input("Primeiro de tudo, como eu te chamo?")

# Só continua se a pessoa digitar um nome
if nome:
    st.write(f"Show de bola, {nome}! Nome bacana.")

    # Pergunta 2: Estado Civil
    estado_civil = st.radio(
        f"E aí, {nome}, na pista ou já achou a tampa da panela?",
        ("Solteiro(a)", "Casado(a)", "Namorando e amando", "É complicado...")
    )

    # Pergunta 3: Idade
    idade = st.slider(
        "Beleza. Agora, sem mentir, quantos anos você tem?",
        min_value=1,
        max_value=100,
        value=18 # Começa em 18
    )

    # Pergunta 4 e 5: Peso e Altura (para a gente poder brincar)
    st.write("Agora uma parte mais... digamos, física. Me fala seu peso e altura pra eu ter uma ideia.")

    # Colocando em colunas pra ficar mais bonito
    col1, col2 = st.columns(2)

    with col1:
        peso = st.number_input("Seu peso (kg)", min_value=0.0, format="%.2f")

    with col2:
        altura = st.number_input("Sua altura (metros, tipo 1.75)", min_value=0.0, format="%.2f")


    # --- Botão para gerar a resposta final ---
    st.markdown("---")

    if st.button(f"Clique aqui pra ver minha análise sincerona, {nome}!"):
        # Verifica se peso e altura foram preenchidos para não dar