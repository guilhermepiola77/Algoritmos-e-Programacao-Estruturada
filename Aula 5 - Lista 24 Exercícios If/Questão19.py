# 19. Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um
# triangulo e se forem, se é um triangulo escaleno, equilátero ou isóscele, considerando
# os seguintes conceitos:
# a. O comprimento de cada lado de um triangulo é menor que a soma dos outros
# dois lados.
# b. Chama-se equilátero o triangulo que tem três lado iguais.
# c. Denominam-se isósceles o triangulo que tem o comprimento de dois lados
# iguais
# d. Recebe o nome de escaleno o triangulo que tem os três lados diferentes.

def verificar_triangulo(A, B, C):
    if A >= B + C or B >= A + C or C >= A + B:
        return "Não é possível formar um triângulo com esses lados."
    elif A == B == C:
        return "É um triângulo equilátero."
    elif A == B or A == C or B == C:
        return "É um triângulo isósceles."
    else:
        return "É um triângulo escaleno."

def main():
    A = float(input("Digite o comprimento do lado A: "))
    B = float(input("Digite o comprimento do lado B: "))
    C = float(input("Digite o comprimento do lado C: "))

    resultado = verificar_triangulo(A, B, C)
    print(resultado)

if __name__ == "__main__":
    main()
