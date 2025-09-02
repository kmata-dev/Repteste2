import time

def fazer_pergunta_sim_nao(pergunta):
    """Função para garantir que o usuário responda 'sim' ou 'não'."""
    while True:
        resposta = input(pergunta).lower().strip()
        if resposta in ["sim", "s"]:
            return "sim"
        elif resposta in ["nao", "não", "n"]:
            return "nao"
        else:
            print("Por favor, responda com 'sim' ou 'não'.")

def questionario_pessoal():
    """Inicia um questionário pessoal interativo."""
    print("Olá! Gostaria de fazer algumas perguntas para nos conhecermos melhor. 😊")
    time.sleep(1)

    # Pergunta sobre o nome
    nome = input("Primeiramente, qual é o seu nome? ")
    print(f"Que nome bonito, {nome}! É um prazer conversar com você.")
    time.sleep(1.5)

    # Pergunta sobre a idade
    while True:
        try:
            idade_str = input("Quantos anos você tem? ")
            idade = int(idade_str)
            if idade <= 0:
                 print("Idade inválida. Por favor, digite um número positivo.")
                 continue
            break
        except ValueError:
            print("Ops! Parece que você não digitou um número. Tente novamente.")

    if idade < 30:
        print(f"{idade} anos! Você está na flor da idade, aproveitando o melhor da vida.")
    else:
        print(f"{idade} anos! Uma ótima fase, com muita experiência e sabedoria acumulada.")
    time.sleep(1.5)

    # Pergunta sobre o peso
    while True:
        try:
            peso_str = input("Se não for muito incômodo, poderia me dizer seu peso em kg? (Ex: 75.5) ")
            peso = float(peso_str.replace(',', '.')) # Aceita tanto ponto quanto vírgula
            if peso <= 0:
                print("Peso inválido. Por favor, digite um valor positivo.")
                continue
            break
        except ValueError:
            print("Formato inválido. Por favor, digite apenas o número do seu peso.")

    print(f"Entendido, {peso} kg. Obrigado por compartilhar! Cuidar da saúde é sempre importante.")
    time.sleep(1.5)

    # Pergunta sobre estado civil
    estado_civil = input("E qual o seu estado civil? (Solteiro(a), Casado(a), etc.) ").lower()

questionario_pessoal()