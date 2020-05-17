def inicio():
    print('-' * 30)
    print(f'{" JOGO DA VELHA ":-^30}')
    print('-' * 30)
    print(f'{"JOGADOR 1: X  JOGADOR 2: O":^30}')
    print('-' * 30)


def placar():
    pass


def interface(tabela):
    i = 0
    for j in range(0, 3):
        for c in range(0, 3):
            print(f'[ {tabela[i]} ]', end='')
            i += 1
        print()
    print('-' * 30)


def verificar(tabela, user):
    interface(tabela)
    if tabela[0] == tabela[1] == tabela[2] or \
            tabela[3] == tabela[4] == tabela[5] or \
            tabela[6] == tabela[7] == tabela[8] or \
            tabela[0] == tabela[3] == tabela[6] or \
            tabela[1] == tabela[4] == tabela[7] or \
            tabela[2] == tabela[5] == tabela[8] or \
            tabela[0] == tabela[4] == tabela[8] or \
            tabela[2] == tabela[4] == tabela[6]:
        print(f'{user:>12} GANHOU!')
        return True
    else:
        return False
