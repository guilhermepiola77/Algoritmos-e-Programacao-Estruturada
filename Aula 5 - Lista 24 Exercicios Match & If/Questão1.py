# 1. Faça um programa que receba dois números e mostra qual deles é o maior.

def encontrar_maior(numero1, numero2):
    if numero1 > numero2:
        return numero1
    elif numero2 > numero1:
        return numero2
    else:
        return "Os números são iguais"


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


maior_numero = encontrar_maior(num1, num2)
print("O maior número é:", maior_numero)
