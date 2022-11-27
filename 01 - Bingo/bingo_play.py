from bingo_function import sorteio
from random import choice as ch

numeros = 7 #Quantidade de números das cartelas
num_max = 30 #Limite de números para o Sorteio

sorteador = list(range(1, num_max + 1))
Cartela_jogador_1 = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]

sorteador = list(range(1, num_max + 1))
Cartela_jogador_2 =  [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]

print(f'Cartela Jogador 1: {Cartela_jogador_1}')
print(f'Cartela Jogador 2: {Cartela_jogador_2}\n')

sorteio(Cartela_jogador_1, Cartela_jogador_2, num_max)