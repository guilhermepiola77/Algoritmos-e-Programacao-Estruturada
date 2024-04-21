# 7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
# números forem iguais, imprima a mensagem “Números iguais”.

def encontrar_maior(num1, num2):
    if num1 > num2:
        print(f"O maior número é: {num1}")
    elif num2 > num1:
        print(f"O maior número é: {num2}")
    else:
        print("Números iguais")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o  segundo número: "))

encontrar_maior(numero1, numero2)