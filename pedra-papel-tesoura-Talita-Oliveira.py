"""Você deverá desenvolver um programa que funcione como o jogo Pedra-Papel-Tesoura.
1. O programa deverá exibir um menu de opções como o da figura abaixo:

2. Após a exibição do menu, o usuário deverá digitar sua opção.
3. O computador irá gerar um número aleatório.
4. O usuário é o primeiro jogador e o computador é o segundo
5. O programa deverá exibir qual foi a opção do jogador e do computador
6. Se você ganhar do computador, a saída será “VOCÊ GANHOU!”
7. Se o computador ganhar de você a saída será “VOCÊ PERDEU!”
8. Se houver empate a saída será “EMPATE!”
9. Se o usuário digitar a opção 4 o programa deve ser finalizado e a mensagem “ATÉ A PRÓXIMA!” deverá ser
exibida
10. Se o usuário digitar um número diferente das opções (1 a 4) uma mensagem “Esta não é uma opção válida!
Digite um número entre 1 e 4” deverá ser exibida
11. Caso o usuário digite algo que não seja um número uma mensagem “Você não sabe brincar. Fim de jogo!”
será exibida e o jogo encerrará.
12. O menu deverá ser exibido enquanto a opção 4 não for digitada pelo usuário ou uma opção inválida.
Regras do jogo:
- Pedra ganha da Tesoura (a amassa e quebra)
- Tesoura ganha do Papel (o corta)
- Papel ganha da Pedra (a embrulha)"""

"""Jogo Pedra-Papel-Tesoura
Aluna: Talita Giovanna Xavier de Oliveira
"""
import random

def menu():
    print("  Pedra - Papel - Tesoura  \n===========================\nMenu de opções:\n1: Pedra\n2: Papel\n3: Tesoura\n4: Sair do Jogo\n")
    numero = input("Digite sua opção: ")
    sorteio = random.randint(1,3)
    entrada(numero, sorteio)

def entrada(numero, sorteio):
    verificar = numero.isdigit()
    if verificar == True:
        numero = int(numero)
        if numero == 1:
            if sorteio == 1:
                print("Jogador: Pedra\nComputador: Pedra")
                resultado(numero, sorteio)
            elif sorteio == 2:
                print("Jogador: Pedra\nComputador: Papel")
                resultado(numero, sorteio)
            else:
                print("Jogador: Pedra\nComputador: Tesoura")
                resultado(numero, sorteio)
        elif numero == 2:
            if sorteio == 1:
                print("Jogador: Papel\nComputador: Pedra")
                resultado(numero, sorteio)
            elif sorteio == 2:
                print("Jogador: Papel\nComputador: Papel")
                resultado(numero, sorteio)
            else:
                print("Jogador: Papel\nComputador: Tesoura")
                resultado(numero, sorteio)
        elif numero == 3:
            if sorteio == 1:
                print("Jogador: Tesoura\nComputador: Pedra")
                resultado(numero, sorteio)
            elif sorteio == 2:
                print("Jogador: Tesoura\nComputador: Papel")
                resultado(numero, sorteio)
            else:
                print("Jogador: Tesoura\nComputador: Tesoura")
                resultado(numero, sorteio)
        elif numero == 4:
            print("ATÉ A PRÓXIMA!")
        elif numero < 1 or numero > 4:
            print("Esta não é uma opção válida!")
            menu()
    else:
        print("Você não sabe brincar. Fim de jogo!")

def resultado(num, sorteado):
    if num == 1:
        if sorteado == 1:
            print("EMPATE!")
        elif sorteado == 2:
            print("VOCÊ PERDEU!")
        else:
            print("VOCÊ GANHOU!")
    elif num == 2:
        if sorteado == 1:
            print("VOCÊ GANHOU!")
        elif sorteado == 2:
            print("EMPATE!")
        else:
            print("VOCÊ PERDEU!")
    elif num == 3:
        if sorteado == 1:
            print("VOCÊ PERDEU!")
        elif sorteado == 2:
            print("VOCÊ GANHOU!")
        else:
            print("EMPATE!")

menu()

