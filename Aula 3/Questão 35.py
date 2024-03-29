# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
# Gere outro numero formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123
# Número Gerado = 321.

numero = int(input("Digite um número inteiro positivo de três digitos (entre 100 e 999): "))

if 100 <= numero <= 999:
    numero_str = str (numero)
    numero_invertido_str = (numero_str[::-1])
    numero_invertido = int(numero_invertido_str)

    print("Número Gerado:",numero_invertido)
else:
    print("O número digitado não possuí três digitos.")

