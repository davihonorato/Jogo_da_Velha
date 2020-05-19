from time import sleep


def inicio():  # Imprime uma interface introdutória do game
    print('-' * 30)
    print(f'{" JOGO DA VELHA ":-^30}')
    print('-' * 30)
    print(f'{"JOGADOR 1: X  JOGADOR 2: O":^30}')
    print('-' * 30)


def placar(usuario):  # Mostra o placar dos jogadores
    # Irá analisar quem venceu e armazenar em algum lugar.
    # Quando chegar no total de 3 vitórias, o placar irá zerar.
    pass


def interface(tabela):  # Imprime uma interface semelhante ao desenho original do game
    i = 0
    for j in range(0, 3):
        for c in range(0, 3):
            print(f'[ {tabela[i]} ]', end='')
            i += 1
        print()
    print('-' * 30)


def verificar(tabela, user):  # Imprime a interface e verifica se alguém conseguiu vencer
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
        print('-' * 30)
        sleep(1)
        placar(user)
        return True
    else:
        return False


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
