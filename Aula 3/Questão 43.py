# 43. O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a
# quantidade de cada item que você consumiu e calcule a conta final.
# a. Hambúrguer................. R$ 3,00
# b. Cheeseburger.............. R$ 2,50
# c. Fritas............................ R$ 2,50
# d. Refrigerante ................. R$ 1,00
# e. Milkshake..................... R$ 3,00

quantidade_hamburguer = int(input("Digite a quantidade de Hambúrgueres consumidos: "))
quantidade_cheeseburger = int(input("Digite a quantidade de Cheeseburgers consumidos: "))
quantidade_fritas = int(input("Digite a quantidade de Fritas consumidas: "))
quantidade_refrigerante = int(input("Digite a quantidade de Refrigerantes consumidos: "))
quantidade_milkshake = int(input("Digite a quantidade de Milkshakes consumidos: "))

preco_hamburguer = 3.00
preco_cheeseburger = 2.50
preco_fritas = 2.50
preco_refrigerante = 1.00
preco_milkshake = 3.00

total = (quantidade_hamburguer * preco_hamburguer) + (quantidade_cheeseburger * preco_cheeseburger) + \
        (quantidade_fritas * preco_fritas) + (quantidade_refrigerante * preco_refrigerante) + \
        (quantidade_milkshake * preco_milkshake)

print("Conta Final: R$", total)
