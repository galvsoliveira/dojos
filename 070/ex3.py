"""
https://www.codewars.com/kata/56a1c074f87bc2201200002e

Escreva uma função que, dado um array `arr`, retorne um novo array contendo,
em cada índice `i`, a quantidade de números estritamente menores que `arr[i]`
à sua direita.

Por exemplo:

* Entrada [5, 4, 3, 2, 1] => Saída [4, 3, 2, 1, 0]
* Entrada [1, 2, 0] => Saída [1, 1, 0]


>>> numeros_menores_a_direita([1,2])
[0, 0]

>>> numeros_menores_a_direita([2,1])
[1, 0]

>>> numeros_menores_a_direita([5, 4, 3, 2, 1])
[4, 3, 2, 1, 0]

>>> numeros_menores_a_direita([1, 2, 0])
[1, 1, 0]


>>> numeros_menores_que(2, [1])
1

>>> numeros_menores_que(1, [1])
0

"""


def numeros_menores_a_direita(lista):
    # resultado=[]
    # for i, item in enumerate(lista):
    #     resultado.append(numeros_menores_que(item, lista[i:]))
    return [numeros_menores_que(item, lista[i:]) for i, item in enumerate(lista)]


def numeros_menores_que(n, lista):
    # total = 0
    # for item in lista:
    #     if item < n:
    #         total+=1
    return len([ item for item in lista if item < n])
