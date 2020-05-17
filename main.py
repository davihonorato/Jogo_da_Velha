from functions import *

inicio()
vit = 0
while True:
    jogador_1 = 'X'
    jogador_2 = 'O'
    placar()
    win = False
    count = 0

    tabela = ['1', '2', '3',
              '4', '5', '6',
              '7', '8', '9']
    interface(tabela)
    while True:
        while True:
            if count % 2 == 0:
                user = jogador_1
                resp = int(input('JOGADOR 1: '))
            else:
                user = jogador_2
                resp = int(input('JOGADOR 2: '))
            if tabela[resp-1].isalpha():
                print('NÃO É POSSIVEL ESSA JOGADA.')
            else:
                tabela[resp - 1] = user
                break
        print('-' * 30)
        win = verificar(tabela, user)
        if win:
            break
        count += 1
    print('-'*30)
    vit += 1
    if vit == 3:
        break
