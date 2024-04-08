# 36. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

numero = int(input("digite o número: "))

u = numero // 1 % 10 
d = numero // 10 % 10 
c = numero // 100 % 10 
m = numero // 1000 % 10 

print("Os números são: {}".format(numero))
print("unidade: {}".format(u))
print("dezena: {}".format(d))
print("centena: {}".format(c))
print("milhar: {}".format(m))
Return = (0)

