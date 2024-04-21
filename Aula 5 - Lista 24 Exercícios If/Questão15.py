# 15. Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
# correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

def imprimir_mes(numero):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

    if numero in meses:
        print("O mês correspondente ao número", numero, "é", meses[numero])
    else:
        print("Número inválido. Deve ser um inteiro entre 1 e 12.")

def main():
    numero = int(input("Digite um número entre 1 e 12: "))
    imprimir_mes(numero)

if __name__ == "__main__":
    main()
