# 11. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número
# inválido”. Se o numero for positivo, calcular o logaritmo deste número.

import math

def calcular_logaritmo(numero):
    if numero <= 0:
        print("Número inválido")
    else:
        resultado = math.log(numero)
        print("O logaritmo do número é:", resultado)

def main():
    numero = int(input("Digite um número inteiro: "))
    calcular_logaritmo(numero)

if __name__ == "__main__":
    main()
