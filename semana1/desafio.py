# -*- coding: utf-8 -*-
"""DESAFIO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kd3-NLeIKwXtKnqt7N34XfZcMD63sQ_S
"""

lista = list(range(0,20,1))

lista_pares = []
lista_impares = []

for numero in lista:

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("La lista generada: ", lista)
print("Lista de numeros pares: ", lista_pares)
print("Lista de numeros impares: ", lista_impares)