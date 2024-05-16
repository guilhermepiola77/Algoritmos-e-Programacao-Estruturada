# '''
# Solicite para o usuário inforar um número e se 
# ele quiser exibir os números pares ou impares.
# Com base no número que ele informar, exiba todos os 
# números pares/impares daquele intervalo.
# Ex:
# Digite um número:
# Exibir pares ou impares ? (P OU I)
# '''

num = int(input("Digite um numero:"))
opcao = input("Exibir pares ou impares ? (P OU N)")

for n in range(1, num + 1):
    if n % 2 == 0:
        if opcao == "p":
            print(f'O {n} é par')
    else:
        if opcao == 'i':
            print(f'O {n} é impar')

    
                    
     



