# 39. Implemente um programa que calculo o ano de nascimento de uma pessoa a partir de
# sua idade e do ano atual.

idade = int(input("Digite a idade da pessoa: "))

ano_atual = int(input("Digite o ano atual: "))

ano_nascimento = ano_atual - idade

print("O ano de nascimento da pessoa é:", ano_nascimento)
