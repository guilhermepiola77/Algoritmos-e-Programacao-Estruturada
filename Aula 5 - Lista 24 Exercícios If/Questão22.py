# 22. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
# possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%.; RJ 15%; MS
# 8%). Faça um programa em que o usuário entre com o valor e o estado destino do
# produto e o programa retorne o preço final do produto acrescido do imposto do
# estado em que ele será vendido. Se o estado digitado não for valido, mostrar uma
# mensagem de erro.

def calcular_preco_final(valor, estado):
    if estado == "MG":
        taxa_imposto = 0.07
    elif estado == "SP":
        taxa_imposto = 0.12
    elif estado == "RJ":
        taxa_imposto = 0.15
    elif estado == "MS":
        taxa_imposto = 0.08
    else:
        print("Erro: Estado inválido.")
        return None

    preco_final = valor * (1 + taxa_imposto)
    return preco_final

def main():
    valor = float(input("Digite o valor do produto: "))
    estado = input("Digite o estado de destino do produto (MG, SP, RJ ou MS): ").upper()

    preco_final = calcular_preco_final(valor, estado)
    if preco_final is not None:
        print("O preço final do produto no estado", estado, "é:", preco_final)

if __name__ == "__main__":
    main()
