# 25. Leia a altura e raio de um cilindro circular e imprima o volume do cilindro. O volume de
# um cilindro circular é calculado por meio da seguinte fórmula: 𝑉 = 𝜋 ∗ 𝑟𝑎𝑖𝑜² onde 𝜋 =
# 3.141592.

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

volume = 3.141592 * (raio**2) * altura 

print("O volume do cilindro é: ",volume)

