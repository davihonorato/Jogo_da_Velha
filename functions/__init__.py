def inicio():  # Imprime uma interface introdutória do game
    print('-' * 30)
    print(f'{" JOGO DA VELHA ":-^30}')
    print('-' * 30)
    print(f'{"JOGADOR 1: X  JOGADOR 2: O":^30}')
    print('-' * 30)


def interface(tabela):  # Imprime uma interface semelhante ao desenho original do game
    i = 0
    for j in range(0, 3):
        for c in range(0, 3):
            print(f'[ {tabela[i]} ]', end='')
            i += 1
        print()
    print('-' * 30)


def verificar(tabela, user):  # Verifica se alguém conseguiu vencer; atualiza as vitorias
    if tabela[0] == tabela[1] == tabela[2] or \
            tabela[3] == tabela[4] == tabela[5] or \
            tabela[6] == tabela[7] == tabela[8] or \
            tabela[0] == tabela[3] == tabela[6] or \
            tabela[1] == tabela[4] == tabela[7] or \
            tabela[2] == tabela[5] == tabela[8] or \
            tabela[0] == tabela[4] == tabela[8] or \
            tabela[2] == tabela[4] == tabela[6]:
        print(f'{user:>12} GANHOU!')
        print('-' * 30)
        return True
    elif velha(tabela):
        print(f'{"DEU VELHA":^30}')
        print('-' * 30)
        return True
    else:
        return False


def velha(tabela):  # Saber se existem opções a serem marcadas e retonar se 'deu velha'(empate) ou não.
    deu_velha = False
    opcoes = 9
    for c in tabela:
        if c.isalpha():
            opcoes -= 1
    if opcoes == 0:
        deu_velha = True
    return deu_velha


def leiaNum(txt):  # Recebe a entrada do usuário
    opcoes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        num = str(input(txt)).strip()
        if num in opcoes:
            try:
                n = int(num)
            except:
                print('Ocorreu um erro.')
            else:
                return n
        else:
            print('Digite um número válido.')
