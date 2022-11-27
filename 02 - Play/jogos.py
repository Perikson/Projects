import forca
import guessing_game
import commun_functions

def escolhe_jogo():
    commun_functions.intro(' Escolha o seu jogo! ')

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        guessing_game.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
