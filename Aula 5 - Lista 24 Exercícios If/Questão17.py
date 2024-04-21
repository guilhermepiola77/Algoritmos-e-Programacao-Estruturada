# 17. Faça um programa que mostre ao usuário um menu com 4 opções de operações
# matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu
# programa então pede dois valores numéricos e realiza a operação, mostrando o
# resultado e saindo.

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero"
    else:
        return num1 / num2

def mostrar_menu():
    print("Menu de operações:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def main():
    mostrar_menu()
    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida.")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = soma(num1, num2)
    elif opcao == '2':
        resultado = subtracao(num1, num2)
    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
    elif opcao == '4':
        resultado = divisao(num1, num2)

    print("Resultado da operação:", resultado)

if __name__ == "__main__":
    main()
