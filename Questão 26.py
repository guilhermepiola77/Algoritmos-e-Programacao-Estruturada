# 26. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
# tendo em vista que o desconto foi de 12%.

valor = float(input("Digite o valor do produto: "))

desconto = (0.12 * valor)
valor_com_desconto = (valor - desconto)

print("O valor do produto com desconto de 12 % é: ",valor_com_desconto)

