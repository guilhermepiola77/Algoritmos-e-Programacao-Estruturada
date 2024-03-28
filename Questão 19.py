# 19. Leia um valor real e a cotação do dólar. Em seguida, imprima o valor correspondente
# em dólares.

valor = float(input("Digite um valor em reais: "))

cotação_dolar = float(input("Digite a cotação do dolar: "))

valor_dolar = valor / cotação_dolar

print("O valor em doláres é:",valor_dolar)