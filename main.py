from functions import inicio

inicio()
jogador_1 = 'X'
jogador_2 = 'O'
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
        if count % 2 == 0:
            user = jogador_1
            resp = int(input('JOGADOR 1: '))
        else:
            user = jogador_2
            resp = int(input('JOGADOR 2: '))
        print(tabela[resp-1])
        if tabela[resp-1].isalpha():
            print('NÃO É POSSIVEL ESSA JOGADA.')
        else:
            tabela[resp - 1] = user
            break
    count += 1
