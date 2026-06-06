import numpy as np

# Exemplos iniciais


def somar(a, b):
    return a + b


def somar_lista(list):
    soma = 0
    for l in list:
        soma += l
    return soma


# Dado um vértice, retorna o grau dele

def calcular_grau(A, indice):
    grau = 0
    for i in range(4):
        grau += A[indice, i]
    return grau


# Matriz de adjacência do C_4

A = np.array([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]])

# Teste
print(calcular_grau(A, 2))


# Retorna a sequência de graus do grafo

def sequencia_graus(A):
    lista = []
    for j in range(4):
        lista.append(calcular_grau(A, j))
    return lista


# Teste para o C_4
print(sequencia_graus(A))


def verificar_adjacencia(indice1, indice2):
    if A[indice1, indice2] == 1:
        return True
    else:
        return False


print(verificar_adjacencia(0, 1))
print(verificar_adjacencia(0, 3))

# Obs: o indice k corresponde ao vértice k + 1 na nossa enumeração
