# Jogo da forca em python!

import os
import random

def forca():

# Os itens da lista de palavras abaixo pode ser alterada conforme sua escolha. Basta alterar o que está dentro das " "

    palavras = ["paralelepipedo", "jogador", "usuario", "python", "vscode", "estudo", "caraguatatuba"]

    print("Jogo da forca!")
    print("1.Lista preparada.\n2.Digite sua palavra.")

# Esse método while verifica qual a dificuldade / modalidade o usuário quer.
# Escolhendo 1, uma palavra aleatória da lista é sorteada.
# Escolhendo 2, o usuário pode escrever uma palavra para outro usuário tentar descobrir.

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

# Essa variável define o tamanho da palavra secreta em "_" para que seja substituída pelas letras da tentativa.
# O número de tentativas também pode ser alterado conforme sua escolha. Coloquei 12, deixando o jogo fácil - mediano. Diminua o número e torne mais desafiador.

    palavra_secreta = ["_"] * len(palavra)
    tentativas = 12

# Nesse método while, substituímos as letras da palavra normal por "_".
# Na condicional if, definimos a tentativa por letra com um laço de repetição for. Se o usuário digitar a letra correta, ela será substituída na posição correspondente.
# Se o usuário digitar errado, é descontada uma tentativa e o usuário tenta novamente.
# O laço for é usado para quando temos um "range" definido. No caso, o range desse laço é o comprimento (len) da própria palavra sorteada.

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

# Importando a biblioteca "os", podemos pedir para o terminal ser limpo após todas as tentativas esgotarem ou a palavra ser desvendada.

    os.system('cls')
    # os.system('clear') - para mac / linux

# Essa condicional if fala que, se não tiver mais nenhum "_", a palavra foi desvendada e você ganhou! Caso contrário, game over :_(

    if "_" not in palavra_secreta:
        print("Parabéns, você descobriu a palavra!")
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

# E por fim, mas não menos importante, um pequeno menu para ilustrar o fim do jogo, dando ao usuário as opções de jogar novamente ou finalizar o programa.
# Em caso de querer jogar novamente, a função forca() é acionada e retorna o código ao começo, dando início a um novo jogo.

    jogar_novamente = input("Deseja jogar novamente? [S / N]: ").upper()
    
    if jogar_novamente == 'S':
        forca()
    else:
        print("Fim do jogo.")

forca()

# Gostou? Tem alguma melhoria a adicionar? Me dê seu feedback por instagram: @massarii07 ou pelo discord: massari.
# Tamo junto! :)
