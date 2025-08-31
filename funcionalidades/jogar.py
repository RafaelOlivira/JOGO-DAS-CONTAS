import random
import os
from .operadores import *
from .salvar_pontuacao import salvar

def jogar():
    pontuacao = 0
    while True:
        os.system('cls')
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operador = random.randint(1,3)
        if operador == 1:
            result = somar(num1,num2)
            operador = "+"
        elif operador == 2:
            result = subtrair(num1,num2)
            operador = "-"
        else:
            result = multiplicar(num1,num2)
            operador = "*"
        print("-="*16)
        print(f"\t {num1} {operador} {num2} = ??")
        print("-="*16)
        entrada_user = int(input("\nDigite o resultado da operação: "))
        if entrada_user == result:
            print("-"*30)
            print("  Parabéns você acertou!")
            print("-"*30)
            pontuacao += 1
            _ = input("Pressione qualquer tecla para continuar...")
        else:
            print("-"*30)
            print(f"Infelizmente você perdeu!! ;C\nPontuação: {pontuacao}")
            print("-"*30)
            nome_jogador = input("Digite seu nome: ")
            salvar(nome_jogador,pontuacao)
            _ = input("Pressione qualquer tecla para continuar...")
            break
            
                