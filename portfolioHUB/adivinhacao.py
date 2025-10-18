14

## 🎯 ETAPA 3 — Projeto pessoal: **Jogo da Adivinhação (Python)**



# adivinhacao.py
# Projeto pessoal: Jogo da adivinhação em Python

import random

print("=== Jogo da Adivinhação ===")
numero_secreto = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 20): "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
