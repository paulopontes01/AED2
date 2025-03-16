"""Jogo da Forca -
Jogo onde o jogador tem que acertar a palavra proposta, tendo como dica o número de letras. Cada letra errada, é desenhado uma parte do corpo do enforcado. O jogo termina com o acerto da palavra ou com o preenchimetnto de todas as partes do corpo do enforcado 1 - 2 - O 3 - O- 4 - O-| 5 - O-|- 6 - O-|-< """

import random
palco = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]

#Classe
class Forca:
    # Metodo Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []

    # Metodo para adivinhar a letra
    def adivinha(self,letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Metodo para veriofocar se o jogo terminou
    def forca_acabou(self):
        if self.forca_venceu() or (len(self.letras_erradas) >= 5):
            return True
        return False

    # Metodo para verificar se o jogador venceu
    def forca_venceu(self):
        if '_' not in self.palavra_escondida():
            return True
        return False

    # Metodo para não mostrar a letra no palco
    def palavra_escondida(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                status += '-'
            else:
                status += letra
        return status

    # Metodo para checar o stauts do jogo e imprimir o palco na tela
    def mostra_status_jogo(self):
        print("\n======= Jogo da Forca =======")
        print(palco[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print('\nLetras Erradas: ')
        for letra in self.letras_erradas:
            print(letra,)
        print('\nLetras Corretas: ')
        for letra in self.letras_certas:
            print(letra,)

# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
    with open("../JogoForca/palavras.txt", "rt") as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

# Função Main - Execução do Programa
def main():
    # Objeto
    jogo = Forca(palavra_aleatoria())

    # Enquanto o jogo não tiver terminado, mostrar o stutus
    # Solciita uma letra e faz a leitura do caracter
    while not jogo.forca_acabou():
        jogo.mostra_status_jogo()
        letra_escolhida = input("\nDigite uma letra: ")
        jogo.adivinha(letra_escolhida)

    # Verifica o status do jogo
    jogo.mostra_status_jogo()

    # De acordo com o status, imprime mensagem na tela par ao usuário
    if jogo.forca_venceu():
        print('\nParabéns! Você ganhou! :)')
    else:
        print('\nFinal do Jogo! Você perdeu. :(')
        print('A palavra era '+ jogo.palavra)

    print('Foi bom jogar com você! \n')

# Executa o programa
if __name__ == "__main__":
    main()
