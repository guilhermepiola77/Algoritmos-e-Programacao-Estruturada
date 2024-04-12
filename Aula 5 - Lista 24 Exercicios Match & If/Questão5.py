# 5. Faça um programa que receba um número inteiro e verificado se este número é par ou
# ímpar.

numero = float(input("Digite um numero: "))
resultado = numero % 2 
if resultado == 0:
    print("O numero é par. ")
else:
    print("O numero é impar: ")

print("O resultado é:{}".format(numero,resultado))

