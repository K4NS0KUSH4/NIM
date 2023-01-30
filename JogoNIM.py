def computador_escolhe_jogada(n, m):
    for i in range(m, 0, -1):
        if (n - i)%(m+1) == 0:
            return i
    if m > n:
        return n
    else:
        return m


def usuario_escolhe_jogada(n, m):
    while True:
        try:
            jogada = int(input('\nQuantas peças você vai tirar? '))
            if 0 < jogada <= m:
                if n >= m:
                    if jogada <= m:
                        return jogada
                else:
                    if jogada <= n:
                        return jogada
            print('\nOops! Jogada Inválida! Tente de novo.')
        except ValueError:
            print('\nPor favor, insira números inteiros para registrar sua jogada.')


def partida():
    while True:
        try:
            valor_n = int(input('\nQuantas peças? '))
            valor_m = int(input('Limite de peças por jogada? '))
        except ValueError:
            print('\nPor favor, insira números inteiros.')
            continue
        if valor_n <= valor_m:
            print('\nO número de peças deve ser maior que o número de peças por jogada.')
        else:
            break
    if valor_n%(valor_m+1) == 0:
        print('\nVocê começa!')
        while True:
            usuario = usuario_escolhe_jogada(valor_n, valor_m)
            if usuario == 1:
                print('Você tirou uma peça.')
            else:
                print(f'Você tirou {usuario} peças.')
            valor_n -= usuario
            if valor_n == 0:
                flag = 0
                break
            if valor_n == 1:
                print('Agora resta apenas uma peça no tabuleiro. ')
            else:
                print(f'Agora restam {valor_n} peças no tabuleiro.')
            computador = computador_escolhe_jogada(valor_n, valor_m)
            if computador == 1:
                print('\nO computador tirou uma peça.')
            else:
                print(f'\nO computador tirou {computador} peças.')
            valor_n -= computador
            if valor_n == 0:
                flag = 1
                break
            if valor_n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            else:
                print(f'Agora restam {valor_n} peças no tabuleiro.')
    else:
        print('\nComputador começa!')
        while True:
            computador = computador_escolhe_jogada(valor_n, valor_m)
            if computador == 1:
                print('\nO computador tirou uma peça.')
            else:
                print(f'\nO computador tirou {computador} peças.')
            valor_n -= computador
            if valor_n == 0:
                flag = 1
                break
            if valor_n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            else:
                print(f'Agora restam {valor_n} peças no tabuleiro.')
            usuario = usuario_escolhe_jogada(valor_n, valor_m)
            if usuario == 1:
                print('Você tirou uma peça.')
            else:
                print(f'Você tirou {usuario} peças.')
            valor_n -= usuario
            if valor_n == 0:
                flag = 0
                break
            if valor_n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            else:
                print(f'Agora restam {valor_n} peças no tabuleiro.')
    if flag == 1:
        print('Fim do jogo! O computador ganhou!')
    else:
        print('Fim do jogo! Você ganhou, mesmo sendo impossível vencer do algoritmo.')
    return flag


def campeonato():
    computador, usuario = 0, 0
    for i in range(3):
        print(f'\n------- Rodada {i+1} -------')
        flag = partida()
        if flag == 1:
            computador += 1
        else:
            usuario += 1
    print('\n------- Final do Campeonato! -------')
    print(f'\nPlacar: Você {usuario} X {computador} Computador')


def main():
    while True:
        print('\nBem vindo ao jogo do NIM! Escolha:')
        print('\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n')
        while True:
            try:
                escolha = int(input('Insira o número correspondente à opção desejada: '))
                if 0 < escolha < 3:
                    break
                else:
                    print('Opção inválida. Tente novamente.')
                    continue
            except ValueError:
                print('Por favor, insira um número inteiro correspondente a uma das opções.')
        if escolha == 1:
            partida()
        else:
            campeonato()
        while True:
            try:
                saida = int(input('\nDigite 0 para sair ou 1 para continuar no programa: '))
                if saida == 0 or saida == 1:
                    break
                else:
                    print('Opção inválida. Tente novamente.')
            except ValueError:
                print('Por favor, insira um número correspondente à opção desejada.')
        if saida == 1:
            continue
        else:
            break


main()
