# Menu principal
import os
import time
from sys import exit
from funcionalidades import jogar
from funcionalidades import ver_pontuacao
while True:
    os.system('cls')
    print("-="*16)
    print("\t Jogo das contas")
    print("-="*16,'\n')

    print("1- Jogar")
    print("2- Ver pontuação")
    print("3- Sair")

    option = int(input("\nEscolha uma opção:"))

    if option < 1 or option > 3: # Ifs para o menu
        os.system('cls')
        print("Opção inválida!")
    elif option == 1:
        jogar.jogar()
    elif option == 2:
        ver_pontuacao.ver_pontuacao()
    elif option == 3:
        exit()
    else:
        time.sleep(1)
        print("A opção é inválida!")