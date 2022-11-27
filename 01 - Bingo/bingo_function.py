from random import choice as ch


def sorteio(cartela_1, cartela_2, num_max):
    num_sorteados = []
    num_iniciais_1 = []
    num_iniciais_2 = []
    vencedor = ''
    sorteador = list(range(1, num_max + 1)) #números a serem sorteados.
    while vencedor == '':

        num_sort = ch(sorteador) #Sorteia um número.
        sorteador.pop(sorteador.index(num_sort)) #Retira o número sorteado da lista de números do bingo.
        num_sorteados.append(num_sort) #Adiciona o número retirado a uma lista de números sorteados.

        if num_sort in cartela_1:
            cartela_1.pop(cartela_1.index(num_sort)) #Retira o numero sorteado da cartela 1
            num_iniciais_1.append(num_sort) #Adiciona o numero sorteado para saber quais números a cartela 1 acertou.
            # Pode ser escrito de maneira mais resumida da seginte maneira:
            # num num_iniciais1.apped(cartela_1.pop(cartela_1.index(num_sort)))

            if len(cartela_1) == 0: #Testa se a cartela_1 ganhou.
                vencedor = 'Jogador 1'
                print(f'Vencedor: {vencedor}')
                print(f'Números da cartela 1: {num_iniciais_1}')
                break

        if num_sort in cartela_2:
            cartela_2.pop(cartela_2.index(num_sort))  # Retira o numero sorteado da cartela 2
            num_iniciais_2.append(num_sort)  # Adiciona o numero sorteado para saber quais números a cartela 2 acertou.
            # Pode ser escrito de maneira mais resumida da seginte maneira:
            # num num_iniciais2.apped(cartela_2.pop(cartela_2.index(num_sort)))

            if len(cartela_2) == 0:  # Testa se a cartela_2 ganhou.
                vencedor = 'Jogador 2'
                print(f'Vencedor: {vencedor}')
                print(f'Números da cartela 2: {num_iniciais_2}')
                break
    print(f'Números Sorteados: {num_sorteados}')


