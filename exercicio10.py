import random


secret_number = random.randint(1, 10)
tentativas = 0

print("Tente adivinhar o número secreto entre 1 e 10!")

while True:
    palpite = input("Digite seu palpite: ")
    try:
        palpite = int(palpite)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    tentativas += 1

    if palpite == secret_number:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
        break
    elif palpite < secret_number:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")