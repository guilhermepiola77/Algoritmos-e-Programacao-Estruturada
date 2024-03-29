# 24. Sejam 𝑏 e 𝑏 os catetos de um triangulo, onde a hipotenusa é obtida pela equação
# ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = √𝑎 2 + 𝑏². Faça um programa que receba os valores de 𝑎 e 𝑏 e calculo
# o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

a = float(input("Digite o valor do cateto a: "))
b= float(input("Digite o valor do cateto b: "))

hip = (a**2 + b**2)

print("O valor da hipotenusa é: ",hip)
