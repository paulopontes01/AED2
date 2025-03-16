"""Jogo da Forca -
Jogo onde o jogador tem que acertar a palavra proposta, tendo como dica o número de letras.
Cada letra errada, é desenhado uma parte do corpo do enforcado.
O jogo termina com o acerto da palavra ou com o preenchimento de todas as partes do corpo do enforcado.

1 - 2 - O
3 - O-
4 - O-|
5 - O-|-
6 - O-|-<
"""

import random

# Representação das partes do corpo no enforcado
palco = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]


# Classe principal do jogo
class Forca:
    def __init__(self, palavra):
        self.palavra = palavra.lower()  # Garante que a palavra esteja em minúsculas
        self.letras_erradas = []
        self.letras_certas = []

    def adivinha(self, letra):
        letra = letra.lower()  # Padroniza a entrada do usuário para minúsculas

        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def forca_acabou(self):
        return self.forca_venceu() or len(self.letras_erradas) >= len(palco) - 1

    def forca_venceu(self):
        return "_" not in self.palavra_escondida()

    def palavra_escondida(self):
        return "".join(letra if letra in self.letras_certas else "_" for letra in self.palavra)

    def mostra_status_jogo(self):
        print("\n======= Jogo da Forca =======")
        print(palco[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print(f'\nLetras Erradas: {", ".join(self.letras_erradas)}')
        print(f'Letras Corretas: {", ".join(self.letras_certas)}')


# Função para escolher uma palavra aleatória de um arquivo
def palavra_aleatoria():
    try:
        with open("palavras.txt", "rt", encoding="utf-8") as f:
            banco = [linha.strip() for linha in f.readlines() if linha.strip()]
        return random.choice(banco) if banco else "python"
    except FileNotFoundError:
        print("Arquivo 'palavras.txt' não encontrado! Usando palavra padrão.")
        return "python"


# Função principal do jogo
def main():
    jogo = Forca(palavra_aleatoria())

    while not jogo.forca_acabou():
        jogo.mostra_status_jogo()
        letra_escolhida = input("\nDigite uma letra: ").strip()

        if len(letra_escolhida) != 1 or not letra_escolhida.isalpha():
            print("Entrada inválida! Digite apenas uma letra.")
            continue

        jogo.adivinha(letra_escolhida)

    jogo.mostra_status_jogo()

    if jogo.forca_venceu():
        print("\nParabéns! Você ganhou! :)")
    else:
        print("\nFinal do Jogo! Você perdeu. :(")
        print(f"A palavra era '{jogo.palavra}'")

    print("Foi bom jogar com você! \n")


# Inicia o jogo
if __name__ == "__main__":
    main()
