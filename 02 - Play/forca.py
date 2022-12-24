import commun_functions
from random import choice as ch


def jogar():
    commun_functions.intro(' Bem vindo ao jogo da Forca! ')

    print('''\nTente descobrir qual é a palavra oculta antes de esgotar todas as suas tentativas.
    
    Escolha o nível de dificuldade:
    
    01 (Fácil) -  7 tentativas.
    02 (Médio) -  5 tentativas.
    03 (Dificil) - 3 tentativas)''')

    l = []
    with open('texto.txt') as doc:
        for p in doc:
            l.append(p.strip())

    palavra_secreta = ch(l)

    print(f'\nPalavra secreta: ', end=' ')

    ps = ['*' for n in range(len(palavra_secreta))]
    for l in ps:
        print(l, end=' ')
    print('\n')

    erro = 1
    tent = 0
    nivel = 0
    while True:

        nivel = int(input('Qual nível você quer tentar: '))
        if nivel == 1:
            tent = 7
            break
        elif nivel == 2:
            tent = 5
            break
        elif nivel == 3:
            tent = 3
            break
        else:
            print('Digite uma opção válida.\n')

    while True:
        print(f'VocÊ possui {tent} tentativas.\n')
        chute = input('Qual letra: ').strip().lower()

        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if chute == letra:
                    ps[i] = letra
        else:
            tent -= 1
            erro += 1

        print('\nPalavra secreta: ')
        for l in ps:
            print(l, end=' ')
        print()

        if nivel == 1:
            commun_functions.desenha_forca_facil(erro)
        elif nivel == 2:
            commun_functions.desenha_forca_medio(erro)
        elif nivel == 3:
            commun_functions.desenha_forca_dificil(erro)

        if tent == 0:
            print(f'A Pavara secreta era: {palavra_secreta}')
            commun_functions.imprime_mensagem_perdedor()
            print("\nFim do jogo")
            break

        comparador = [n for n in palavra_secreta]
        if ps == comparador:
            commun_functions.imprime_mensagem_vencedor()
            break

if (__name__ == "__main__"):
    jogar()
