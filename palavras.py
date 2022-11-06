palavras = []


def gerenciar_palavras():
    def escrever_palavras_no_arquivo():
        with open("palavras.txt", "w", encoding="utf-8") as arquivo:
            for palavra in palavras:
                arquivo.write(f"{palavra}\n")

    def ler_palavras_no_arquivo():
        global palavras
        filename = "palavras.txt"
        with open(filename, "r", encoding="utf-8") as file:
            palavras = []
            for i in file.readlines():
                palavra = i.strip()
                palavras.append(palavra)

    def adicionar_palavra_na_memoria():
        global palavras
        pronto = False
        palavra = input("Qual a palavra a ser adicionada? ")
        palavras.append(palavra)
        while not pronto:
            continuar = input("Deseja adicionar mais uma palavra? ('sim' ou 'nao')")
            if continuar == "sim":
                palavra = input("Qual a palavra a ser adicionada? ")
                palavras.append(palavra)
            else:
                pronto = True

    def mostrar_palavras_na_memoria():
        if len(palavras) >= 1:
            print("Palavras Cadastradas:")
            for palavra in palavras:
                print(f"{palavra}")
        else:
            print("Você ainda não cadastrou nenhuma palavra!")

    pronto = False

    while not(pronto):
        print("""
    -*- Gerenciar Palavras -*-
    Escolha o que deseja fazer:
    0. Voltar
    1. Adicionar Palavra
    2. Listar Palavras
    3. Ler Arquivo
    4. Escrever no Arquivo
        """)
        try:
            valor = int(input("\n       O que deseja fazer? "))
            if 0 <= valor <= 4:
                opcao = valor
            else:
                opcao = 9
                print("Valor inválido, digite um número entre 0 e 4!")
        except ValueError:
            break
        if opcao == 0:
            break
        elif opcao == 1:
            adicionar_palavra_na_memoria()
        elif opcao == 2:
            mostrar_palavras_na_memoria()
        elif opcao == 3:
            ler_palavras_no_arquivo()
        elif opcao == 4:
            escrever_palavras_no_arquivo()

