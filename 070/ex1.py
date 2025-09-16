"""
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

O primeiro século vai do ano 1 até 100 (inclusive), o segundo do 101 até 200 (inclusive), e assim por diante.
Tarefa:
Dado um ano, retorne o século em que ele se encontra.
Exemplos:

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20

>>> seculo(1705)
18

>>> seculo(1601)
17

>>> seculo(1600)
16

>>> seculo(100)
1

>>> seculo(2000)
20

>>> seculo(10000)
100

>>> seculo(10001)
101

>>> seculo(10)
1

>>> seculo(1)
1

>>> seculo(777777)
7778

"""

def seculo(ano):
    return (ano + 99) // 100