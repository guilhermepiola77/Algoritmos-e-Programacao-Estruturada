# 16. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: 𝐴 =
# (𝑏𝑎𝑠𝑒𝑚𝑎𝑖𝑜𝑟+𝑏𝑎𝑠𝑒𝑚𝑒𝑛𝑜𝑟∗𝑎𝑙𝑡𝑢𝑟𝑎
# 2
# , lembre-se que a base maior e a base menor devem ser
# números maiores que zero.

def calcular_area_trapezio(base_maior, base_menor, altura):
    if base_maior <= 0 or base_menor <= 0:
        print("Erro: A base maior e a base menor devem ser números maiores que zero.")
        return None
    else:
        area = ((base_maior + base_menor) * altura) / 2
        return area

def main():
    base_maior = float(input("Digite o valor da base maior do trapézio: "))
    base_menor = float(input("Digite o valor da base menor do trapézio: "))
    altura = float(input("Digite o valor da altura do trapézio: "))

    area = calcular_area_trapezio(base_maior, base_menor, altura)
    if area is not None:
        print("A área do trapézio é:", area)

if __name__ == "__main__":
    main()
