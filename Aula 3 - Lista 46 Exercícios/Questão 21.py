# 21. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor
# de seu dobro.

numero = int(input("Digite um número inteiro: "))

triplo = numero * 3 
dobro = numero * 2

sucessor_triplo = triplo + 1
antecessor_dobro = dobro - 1

soma = sucessor_triplo + antecessor_dobro

print("A soma do sucessor do triplo com o antecessor do dobro é: " ,soma)




