import jogo
import palavras
import jogadores

while True:
    print("""
    -*- -*- -*- Esquartejado -*- -*- -*-
    Bem vindo ao Esquartejado! Escolha o que deseja fazer:

    0. Sair
    1. Jogar com as palavras carregadas.
    2. Gerenciar/carregar palavras.
    3. Ver o ranking de jogadores.
    """)
    try:
        valor = int(input("\n       O que deseja fazer? "))
        if 0 <= valor <= 3:
            opcao = valor
        else:
            opcao = 9
            print("Valor inválido, digite um número entre 0 e 3!")
    except ValueError:
        break
    if opcao == 0:
        break
    elif opcao == 1:
        jogo.jogar()
    elif opcao == 2:
        palavras.gerenciar_palavras()
    elif opcao == 3:
        jogadores.mostrar_ranking_jogadores()
