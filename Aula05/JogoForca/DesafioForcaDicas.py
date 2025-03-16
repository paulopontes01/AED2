import random

# Representação do enforcado em diferentes estágios
palco = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]

# Classe principal do jogo
class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []

    def adivinha(self, letra):
        """Verifica se a letra está na palavra"""
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def forca_acabou(self):
        """Verifica se o jogo acabou"""
        return self.forca_venceu() or len(self.letras_erradas) >= 5

    def forca_venceu(self):
        """Verifica se o jogador venceu"""
        return "_" not in self.palavra_escondida()

    def palavra_escondida(self):
        """Mostra a palavra parcialmente descoberta"""
        return "".join(letra if letra in self.letras_certas else "_" for letra in self.palavra)

    def mostra_status_jogo(self):
        """Exibe o estado atual do jogo"""
        print("\n======= Jogo da Forca =======")
        print(palco[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print(f'Letras Erradas: {", ".join(self.letras_erradas)}')
        print(f'Letras Corretas: {", ".join(self.letras_certas)}')


def palavra_aleatoria():
    """Lê uma palavra e uma dica aleatória do arquivo"""
    try:
        with open("palavras.txt", "rt", encoding="utf-8") as f:
            banco = [linha.strip().split(";") for linha in f.readlines() if linha.strip()]

        if not banco:
            print("⚠️ O arquivo 'palavras.txt' está vazio! Usando palavra padrão.")
            return "python", "Uma linguagem de programação"

        return random.choice(banco)  # Escolhe um par (palavra, dica)

    except FileNotFoundError:
        print("❌ ERRO: O arquivo 'palavras.txt' não foi encontrado!")
        return "python", "Uma linguagem de programação"

    except Exception as e:
        print(f"❌ ERRO ao abrir 'palavras.txt': {e}")
        return "python", "Uma linguagem de programação"


def main():
    """Executa o jogo"""
    palavra, dica = palavra_aleatoria()
    jogo = Forca(palavra)

    print(f"\nDica: {dica}")  # Mostra a dica ao jogador

    while not jogo.forca_acabou():
        jogo.mostra_status_jogo()
        letra_escolhida = input("\nDigite uma letra: ").lower()

        # Verifica se o input é válido
        if not letra_escolhida.isalpha() or len(letra_escolhida) != 1:
            print("⚠️ Digite apenas uma letra válida!")
            continue

        jogo.adivinha(letra_escolhida)

    jogo.mostra_status_jogo()

    if jogo.forca_venceu():
        print('\n🎉 Parabéns! Você ganhou! :)')
    else:
        print('\n😞 Final do Jogo! Você perdeu.')
        print(f'A palavra era: {palavra}')

    print('Foi bom jogar com você! 👋\n')


if __name__ == "__main__":
    main()
