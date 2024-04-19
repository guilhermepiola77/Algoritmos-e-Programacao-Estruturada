# 7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
# números forem iguais, imprima a mensagem “Números iguais”.

def encontrar_maior(num1, num2):
    if num1 > num2:
        print(f"O maior número é: {num1}")
    elif num2 > num1:
        print(f"O maior número é: {num2}")
    else:
        print("Números iguais")

# Solicita ao usuário para inserir os números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chama a função para encontrar o maior número
encontrar_maior(numero1, numero2)
