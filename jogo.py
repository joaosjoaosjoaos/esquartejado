import random
import palavras
import jogadores


def jogar():
    def iniciar():
        palavra = random.choice(palavras.palavras)
        tentativas = 0
        chances = 4
        erros = 0
        pontos = 0
        letras_escolhidas = []
        estado_atual = ["_"] * len(palavra)
        jogador = input("Qual é o seu nome? ")

        print(f"""
    -*- Bem vindo {jogador}! -*-
    Seu objetivo é tentar acertar a palavra secreta, você terá que tentar uma letra por vez, caso você acerte, a letra será colocada na palavra para que você chegue mais perto de acertar, caso você erre, você perderá uma chance, você tem no máximo 4 tentativas.
        """)
        while tentativas < chances and "".join(estado_atual) != palavra:
            letra = input("\n\n     Qual letra você quer tentar? ")
            while letra in letras_escolhidas:
                print("Você escolheu uma letra que já tinha tentado, escolha outra!")
                letra = input("\n     Qual letra você quer tentar? ")
            letras_escolhidas.append(letra)
            if letra in palavra:
                print("Parabéns, você acertou a letra!")
                for i in range(len(palavra)):
                    if letra == palavra[i]:
                        pontos = pontos + 1
                        estado_atual[i] = letra
            else:
                print("Que pena, você errou!")
                erros = erros + 1
                tentativas = tentativas + 1
            print(f"Você já fez {tentativas} tentativas erradas e ainda tem {chances - tentativas} tentativas")
            print("Esse é o estado atual:")
            print(estado_atual)

        jogadores.jogadores.append(jogador)
        jogadores.palavras.append(palavra)
        jogadores.erros.append(erros)
        jogadores.pontos.append(pontos)

    if len(palavras.palavras) < 1:
        print("Você ainda não carregou nenhuma palavra!")
    else:
        iniciar()

