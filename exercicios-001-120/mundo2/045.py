import random

escolhas = ["pedra", "papel", "tesoura"]
escolha_computador = random.choice(escolhas)
opcao = int(input("""
1 - pedra
2 - papel
3 - tesoura

Qual sua escolha? """))

if opcao == 1:
    escolha_usuario = "pedra"

elif opcao == 2:
    escolha_usuario = "papel"

elif opcao == 3:
    escolha_usuario = "tesoura"

else:
    print("Opçao inválida")

if escolha_usuario == escolha_computador:
    print(f"Empate! Vocês dois escolheram {escolha_usuario}")

elif escolha_usuario == "pedra" and escolha_computador == "papel":
    print(f"Você perdeu! \nVocê escolheu {escolha_usuario} e o computador escolheu {escolha_computador}.")

elif escolha_usuario == "papel" and escolha_computador == "tesoura":
    print(f"Você perdeu! \nVocê escolheu {escolha_usuario} e o computador escolheu {escolha_computador}.")

elif escolha_usuario == "tesoura" and escolha_computador == "pedra":
    print(f"Você perdeu! \nVocê escolheu {escolha_usuario} e o computador escolheu {escolha_computador}.")

else:
    print(f"Você ganhou! \nVocê escolheu {escolha_usuario} e o computador escolheu {escolha_computador}.")
