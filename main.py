from functions import *

inicio()
vitorias = 0
while vitorias < 3:
    placar()
    win = False
    count = 0

    tabela = ['1', '2', '3',
              '4', '5', '6',
              '7', '8', '9']
    interface(tabela)
    while win is False:
        while True:
            if count % 2 == 0:
                user = 'X'
                resp = leiaNum('JOGADOR 1: ')
            else:
                user = 'O'
                resp = leiaNum('JOGADOR 2: ')
            if tabela[resp-1].isalpha():
                print('NÃO É POSSIVEL ESSA JOGADA.')
            else:
                tabela[resp - 1] = user
                print('-' * 30)
                break
        count += 1
        win = verificar(tabela, user)
    vitorias += 1
