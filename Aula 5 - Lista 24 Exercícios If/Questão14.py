# 14. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
# da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e
# assim por diante.

def imprimir_dia_da_semana(numero):
    dias_da_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }

    if numero in dias_da_semana:
        print("O dia da semana correspondente ao número", numero, "é", dias_da_semana[numero])
    else:
        print("Número inválido. Deve ser um inteiro entre 1 e 7.")

def main():
    numero = int(input("Digite um número entre 1 e 7: "))
    imprimir_dia_da_semana(numero)

if __name__ == "__main__":
    main()
