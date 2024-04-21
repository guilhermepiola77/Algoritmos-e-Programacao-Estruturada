# 6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
# assim como a diferença existente entre ambos.

def encontrar_maior_e_diferenca(num1, num2):
    if num1 > num2:
        maior = num1
        diferenca = num1 - num2
    elif num2 > num1:
        maior = num2
        diferenca = num2 - num1
    else:
        print("Os números são iguais.")
        return
    
    print(f"O maior número é {maior} e a diferença entre eles é {diferenca}.")

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

encontrar_maior_e_diferenca(numero1, numero2)