import random
import commun_functions

def jogar():
    commun_functions.intro(' Bem vindo ao Jogo de Adivinhação ')

    print('\nEscolha o nível de dificuldade?')
    print('(1) Fácil - Número entre 1 e 100'
          '\n(2) Médio - Número entre 1 e 500'
          '\n(3) Difícil - Número entre 1 e 1000')

    while True:
        nivel = int(input('\nDefina o nível: '))
        if nivel == 1:
            numero_secreto = random.randint(1, 100)
            break
        elif nivel == 2:
            numero_secreto = random.randint(1, 500)
            break
        elif nivel == 3:
            numero_secreto = random.randint(1, 1000)
            break
        else:
            print('Escolha entre os níveis de dificuldade (1) Fácil, (2) Médio ou (3) Difícil.')

    while True:
        total_de_tentativas = int(input('Quantas tentativas você quer ter?'
                                        '\nEscolha entre 1 e 10.: '))
        if total_de_tentativas >= 1 and total_de_tentativas <= 10:
            break


    for rodada in range(1, total_de_tentativas + 1):
        print(f'\nTentativa {rodada} de {total_de_tentativas}')
        chute = int(input('Qual o seu palpite? '))

        if chute == numero_secreto:
            print(f'Parabéns. Você acertou. O número secreto é {numero_secreto}')
            print(f'Você acertou em {rodada} tentativas.')
            break
        elif chute < numero_secreto:
            print(f'Você chutou um número menor.')
        else:
            print(f'Você chutou um número maior.')

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()