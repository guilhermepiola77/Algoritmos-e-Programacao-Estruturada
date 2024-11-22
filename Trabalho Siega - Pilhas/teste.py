def gerenciar_pilha():
    pilha = []
    tamanho_maximo = 10 

    while True:
        print("\nOperações disponíveis:")
        print("a) Empilhar")
        print("b) Desempilhar")
        print("c) Sair")

        opcao = input("Digite a opção desejada: ").lower()

        if opcao == 'a':
            if len(pilha) >= tamanho_maximo:
                print("A pilha está cheia!")
            else:
                elemento = input("Digite o elemento a ser empilhado: ")
                pilha.append(elemento)
                print(f"Elemento '{elemento}' empilhado com sucesso.")

        elif opcao == 'b':
            if not pilha:
                print("A pilha está vazia!")
            else:
                elemento = pilha.pop()
                print(f"Elemento '{elemento}' desempilhado com sucesso.")

        elif opcao == 'c':
            if pilha:
                print(f"O elemento no topo da pilha é: '{pilha[-1]}'")
            else:
                print("A pilha está vazia.")
            break

        else:
            print("Opção inválida!")

def eh_palindromo(palavra):
    pilha = []

    for letra in palavra:
        pilha.append(letra)

    palavra_invertida = ""
    while pilha:
        palavra_invertida += pilha.pop()

    return palavra == palavra_invertida

gerenciar_pilha()

palavra = input("\nDigite uma palavra para verificar se é um palíndromo: ")
if eh_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
