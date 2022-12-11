import commun_functions


def jogar():
    commun_functions.intro(' Bem vindo ao jogo da Forca! ')

    print('''\nTente descobrir qual é a palavra oculta antes de esgotar todas as suas tentativas.
    
    Escolha o nível de dificuldade:
    
    01 (Fácil) -  7 tentativas.
    02 (Médio) -  5 tentativas.
    03 (Dificil) - 3 tentativas)''')

    palavra_secreta = 'banana'.lower()
    print(f'\nPalavra secreta: ', end=' ')

    ps = ['*' for n in range(len(palavra_secreta))]
    for l in ps:
        print(l, end=' ')
    print('\n')

    tent = 0
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

        print('\nA palavra secreta é: ')
        for l in ps:
            print(l, end=' ')
        print()

        if tent == 0:
            print('Você perdeu.')
            print("\nFim do jogo")
            break

        comparador = [n for n in palavra_secreta]
        if ps == comparador:
            print('Parabéns, Você venceu.')
            break

if (__name__ == "__main__"):
    jogar()
