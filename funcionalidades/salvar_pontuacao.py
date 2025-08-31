from .jogar import *

def salvar(nome_jogador,pontuacao):
    with open("pontuacao.txt","a") as arq:
        jogador = "Jogador: "+nome_jogador+" "+"Pontuacao: "+str(pontuacao)+"\n"
        arq.write(jogador)