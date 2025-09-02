import streamlit as st
import time

# --- Configuração da Página ---
st.set_page_config(page_title="Um Robô Curioso...", layout="centered")

# --- Início do App ---
st.title("E aí, Pamela! Bora conversar um pouquinho?")
st.write("O Kelver me contou umas coisas sobre você, mas fiquei curioso pra saber pela sua própria versão... hehe")
st.write(
    "Sou um robô que ele programou, então pode confiar e responder aqui, nosso papo fica só entre nós (e ele, claro).")
st.markdown("---")

# Já sabemos o nome, então vamos usar diretamente
nome = "Pamela"

# Pergunta 1: Estado Civil
estado_civil = st.radio(
    f"Pra começar, o Kelver não me falou o principal... Como tá o coração?",
    ("Solteira", "Casada", "Namorando", "É complicado...")
)

# Pergunta 2: Idade
idade = st.slider(
    "Outra coisa que ele não disse é a sua idade (prometo que não conto pra ninguém 😉).",
    min_value=1,
    max_value=100,
    value=25  # Começa em 25
)

# Pergunta 3 e 4: Peso e Altura
st.write("Ele falou que você se cuida bastante, então me fala aí...")

# Colocando em colunas
col1, col2 = st.columns(2)
with col1:
    peso = st.number_input("Seu peso (kg)", min_value=0.0, format="%.2f")

with col2:
    altura = st.number_input("Sua altura (metros, tipo 1.65)", min_value=0.0, format="%.2f")

# --- Botão para gerar a resposta final ---
st.markdown("---")

if st.button(f"Clique aqui pra ver o que eu descobri sobre você!"):
    # Verifica se peso e altura foram preenchidos
    if peso > 0 and altura > 0:
        with st.spinner("Processando tudo que você me contou..."):
            time.sleep(3)

        st.success(f"Prontinho, {nome}! Aqui está o meu resumo sobre você:")

        # --- Respostas Interativas e Personalizadas ---

        # Resposta sobre Estado Civil (COM A PEGADINHA!)
        if estado_civil == "Solteira":
            st.error(
                "🚨 **Solteira? Como assim?!** Acho que o Kelver não vai gostar NADA de saber disso... É melhor vocês conversarem! hehe 😉")
        elif estado_civil == "Casada":
            st.info(
                "💍 **Casada?** Ah, que legal! O Kelver te admira muito, e com certeza deseja toda a felicidade do mundo pra você!")
        elif estado_civil == "Namorando":
            st.info(
                "❤️ **Namorando?** Ufa, essa é a resposta certa! O Kelver já estava ficando preocupado aqui. Vocês formam um belo casal!")
        elif estado_civil == "É complicado...":
            st.info("🤔 **'É complicado'**... A vida às vezes é assim mesmo. O importante é estar bem, né?")

        # Resposta sobre Idade
        if idade <= 20:
            st.info(
                f"🥳 **{idade} aninhos?** Super nova! Cheia de energia e com a vida toda pela frente. Fase incrível!")
        elif idade <= 30:
            st.info(
                f"🤩 **Na casa dos {idade}, hein?** Considerada por muitos a melhor fase da vida! Aproveite cada segundo.")
        else:
            st.info(
                f"😉 **Com {idade} anos.** Já com uma boa bagagem de vida e muita história pra contar. Isso é muito legal!")

        # Resposta sobre Peso/Altura (com uma pegada mais gentil)
        imc = peso / (altura ** 2)
        if imc < 18.5:
            st.warning(
                f"🏋️ **Sobre se cuidar:** Me parece que você tem uma ótima genética! Só não esquece de se alimentar bem pra manter essa energia toda, ok?")
        elif imc < 24.9:
            st.success(
                f"💪 **Sobre se cuidar:** O Kelver tinha razão, você se cuida super bem! Seu IMC de {imc:.1f} mostra que está tudo em equilíbrio. Parabéns pela dedicação!")
        else:
            st.warning(
                f"🏃 **Sobre se cuidar:** Sinal de que você aproveita as coisas boas da vida! Manter o equilíbrio é sempre bom, e o importante é se sentir bem e saudável.")

        st.markdown("---")
        st.header(f"Conclusão do Robô:")
        st.write(
            f"**{nome}, foi um prazer te conhecer um pouco melhor! Agora sei por que o Kelver fala tanto de você. Ele realmente te acha uma pessoa incrível.** 😉")
        st.balloons()

    else:
        st.error(
            "Opa! Parece que você esqueceu de preencher o peso ou a altura. Preenche lá pra eu poder terminar minha análise!")