from .jogar import *
import sqlite3

def add_banco(nome_jogador,pontuacao):
    conexao = sqlite3.connect("db_jogo.db")
    conexao.execute("insert into placar (nome,pontuacao) values(?,?);",
                    (nome_jogador,pontuacao))
    conexao.commit()
    conexao.close()