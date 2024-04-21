# 9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
# prestação for maior que 20% do salário imprima: “Empréstimo não concedido”, caso
# contrário imprima: “Empréstimo concedido”.

def verificar_emprestimo(salario, prestacao):
    limite_prestacao = salario * 0.2
    if prestacao > limite_prestacao:
        print("Empréstimo não concedido")
    else:
        print("Empréstimo concedido")

def main():
    salario = float(input("Digite o salário do trabalhador: "))
    prestacao = float(input("Digite o valor da prestação do empréstimo: "))

    verificar_emprestimo(salario, prestacao)

if __name__ == "__main__":
    main()
