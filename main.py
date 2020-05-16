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
    while True:
        i = 0
        for j in range(0, 3):
            for c in range(0, 3):
                print(f'[ {tabela[i]} ]', end='')
                i += 1
            print()
        print('-' * 30)
        while True:
            if tabela[0] == tabela[1] == tabela[2] or tabela[3] == tabela[4] == tabela[5] or tabela[6] == tabela[7] == tabela[8]:
                print(f'{user} GANHOU!')
                win = True
            elif tabela[0] == tabela[3] == tabela[6] or tabela[1] == tabela[4] == tabela[7] or tabela[2] == tabela[5] == tabela[8]:
                print(f'{user} GANHOU!')
                win = True
            elif tabela[0] == tabela[4] == tabela[8] or tabela[2] == tabela[4] == tabela[6]:
                print(f'{user} GANHOU!')
                win = True
            break
        if win:
            break
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
        count += 1
    print('-'*30)
    vit += 1
    if vit == 3:
        break
