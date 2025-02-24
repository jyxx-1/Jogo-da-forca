# Jogo da forca em python!

import os
import random

def forca():

    palavras = ["paralelepipedo", "jogador", "usuario", "python", "vscode", "estudo", "caraguatatuba"]

    print("Jogo da forca!")
    print("1.Lista preparada.\n2.Digite sua palavra.")

    while True:
        dificuldade = int(input("Escolha a dificuldade [1 / 2]: "))

        if dificuldade == 1:
            palavra = random.choice(palavras)
            break
        elif dificuldade == 2:
            palavra = input("Digite uma palavra: ").lower()
            break
        else:
            print("Digite um valor válido para escolher a dificuldade!")

    palavra_secreta = ["_"] * len(palavra)
    tentativas = 12

    while "_" in palavra_secreta and tentativas > 0:
        letra = input("Digite uma letra: ").lower()
        print(tentativas)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_secreta[i] = letra
            
            print("Palavra: ", " ".join(palavra_secreta))
        else:
            tentativas -= 1
            print(f"Errou! Tente novamente. {tentativas} restantes!")

    os.system('cls')
    # os.system('clear') - para mac / linux

    if "_" not in palavra_secreta:
        print("Parabéns, você descobriu a palavra!")
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

    jogar_novamente = input("Deseja jogar novamente? [S / N]: ").lower()
    
    if jogar_novamente == 'S':
        forca()
    else:
        print("Fim do jogo.")

forca()        