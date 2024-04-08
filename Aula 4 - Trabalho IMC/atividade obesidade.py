# Solicite para o usuario informar:
#     - Nome
#     - Altura (cm)
#     - Peso (kg)
#     Com base nestes dados realize o calculo para 
#     descobrir qual o IMC (indice de massa corporal)
#     da pessoa.
#     Para o calculo utilize a tabela padrão do IMC.
#     abaixo de 18,5 - Abaixo do Peso (Pegue suplementos do Cariani)
#     entre 18,6 e 24,9 - Peso Ideal (Para Bens)
#     entre 25,0 e 29,9 - Sobrepeso
#     entre 30,0 e 34,9 - Obesidade Grau 1
#     entre 35,0 e 39,9 - Obesidade Grau 2
#     acima de 40,0 - Obesidade Grau 3 (Dr. Nowzaradan te espera)                  
#     formula: IMC = peso / altura²

nome = input("Informe o nome: ")
altura = float(input("Informe  a altura: "))
peso = float(input("Informe o peso: "))

if peso <= 18.5:
    print("Abaixo do peso (Pegue o suplementos do Cariani)")
elif peso >= 18.6 and peso <= 24.9:
    print("Peso ideal (Para Bens)")
elif peso >= 25.0 and peso <= 29.9:
    print("Sobrepeso")
elif peso >= 30.0 and peso <= 34.9:
    print("Obesidade Grau 1")
elif peso >= 35.0 and peso <= 39.9:
    print("Obesidade Grau 2")
else: 
    peso >= 40.0
    print("Obesidade Grau 3 (Dr. Nowzaradan te espera).")

 
IMC = peso / (altura ** 2)

texto=f'''O nome da pessoa é: {nome}
A altura é: {altura}
O peso é: {peso}'
O valor do calculo é: {IMC}'''

print(texto)


    

