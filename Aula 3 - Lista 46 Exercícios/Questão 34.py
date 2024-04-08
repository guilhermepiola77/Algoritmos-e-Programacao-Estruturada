# 34. Faça um programa para converter uma letra maiúscula em letra minúscula. Use a
# tabela ASCII para resolver o problema.

letra_maiuscula = input("Digite uma letra maiscula: ")

valor_ascii = ord(letra_maiuscula)
valor_minusc = (valor_ascii + 32 )

letra_maiuscula = chr(valor_minusc)

print("A letra minuscula correspondente é: ",letra_maiuscula)

