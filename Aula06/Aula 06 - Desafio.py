class Stack:
    """Classe que implementa uma pilha (Stack) usando uma lista"""

    def __init__(self):
        """Inicializa a pilha vazia"""
        self.itens = []

    def is_empty(self):
        """Verifica se a pilha está vazia"""
        return self.itens == []

    def push(self, item):
        """Adiciona um elemento ao topo da pilha"""
        self.itens.append(item)

    def pop(self):
        """Remove e retorna o elemento do topo da pilha"""
        return self.itens.pop()

    def peek(self):
        """Retorna o elemento do topo da pilha sem removê-lo"""
        return self.itens[-1]

    def size(self):
        """Retorna o número de elementos na pilha"""
        return len(self.itens)


def is_balanced(expression):
    """
    Função que verifica se os parênteses, colchetes e chaves em uma string estão balanceados e ordenados corretamente.

    :param expression: String contendo os caracteres a serem analisados.
    :return: True se estiver balanceado, False caso contrário.
    """
    stack = Stack()  # Criamos uma pilha para armazenar os símbolos de abertura
    pairs = {')': '(', ']': '[', '}': '{'}  # Mapeamos os símbolos de fechamento para os de abertura correspondentes

    for char in expression:
        if char in "({[":
            stack.push(char)  # Se for um caractere de abertura, empilhamos
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False  # Se a pilha estiver vazia ou houver um erro de correspondência, retorna False

    return stack.is_empty()  # Se a pilha estiver vazia no final, a expressão está balanceada


# 🚀 Entrada do usuário para testar qualquer sequência
expression = input("Digite a sequência para verificação: ")  # O usuário digita uma string
result = is_balanced(expression)  # Chamamos a função para verificar se está balanceado
print(f"A sequência '{expression}' está balanceada? {result}")  # Exibe o resultado
