import os
def ver_pontuacao():
    os.system('cls')
    with open("pontuacao.txt","r") as arq:
        print(arq.read())
    _ = input("Pressione qualquer tecla para continuar...")