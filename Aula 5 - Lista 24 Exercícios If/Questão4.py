# 4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# a. O número digitado ao quadrado
# b. A raiz quadrada do número digitado

import math

def calculadora_numero_positivo(numero):
    if numero >0:

        quadrado = numero ** 2
        print("O quadrado do número digitado é:", quadrado)

        raiz_quadrada = math.sqrt(numero)
        print("A raiz quadrada do número digitado é:", raiz_quadrada)

    else:
        print("O número digitado não é positivo.")

numero = float(input("Digite um número: "))

calculadora_numero_positivo(numero)