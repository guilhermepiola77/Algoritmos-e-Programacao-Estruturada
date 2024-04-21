# 10. Escreva um programa que leia um número inteiro maior do que zera e devolva, na
# tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá
# o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa
# terminará com a mensagem “Número inválido”.

def soma_algarismos(numero):
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    return soma

def main():
    numero = int(input("Digite um número inteiro maior que zero: "))
    if numero <= 0:
        print("Número inválido")
    else:
        resultado = soma_algarismos(numero)
        print("A soma dos algarismos é:", resultado)

if __name__ == "__main__":
    main()

