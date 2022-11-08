jogadores = []
palavras = []
erros = []
pontos = []

with open("jogadores.txt", "w", encoding="utf-8") as arquivo:
    for jogador in jogadores:
        arquivo.write(f"{jogador}\n")
with open("jogadores.txt", "r", encoding="utf-8") as file:
    jogadores = []
    for i in file.readlines():
        jogador = i.strip()
        jogadores.append(jogador)

def mostrar_ranking_jogadores():
    print("-*- Ranking de Jogadores -*-")
    for jogador in jogadores:
        print(f"{jogador}: {pontos[jogadores.index(jogador)]} pontos, palavra: {palavras[jogadores.index(jogador)]}, erros: {erros[jogadores.index(jogador)]}")

