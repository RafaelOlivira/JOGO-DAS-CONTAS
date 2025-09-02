import os
import sqlite3 
def ver_pontuacao():
    os.system('cls')
    conexao = sqlite3.connect("db_jogo.db")
    cursor = conexao.cursor()
    cursor.execute("select * from placar")
    rs = cursor.fetchall()
    if len(rs) == 0:
        print("Nenhum placar a ser mostrado!")
    else:
        print("Pontuação      Nome        Placar")
        for dados in rs:
            ide,nome,pontuacao = (dados)
            print(f"    {ide}          {nome}         {pontuacao}")
    _ = input("\n\nPressione qualquer tecla para continuar...")