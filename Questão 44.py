# 44. Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês
# mais uma comissão de R$ 50,00 para cada carro vendido e mais 5% do valor da venda.
# Elabore um algoritmo para calcular e imprimir o salário do vendedor num dado mês
# recebendo como dados de entrada o nome do vendedor, o número de carros vendidos
# e o valor total das vendas.

nome_vendedor = input("Digite o nome do vendedor: ")

carros_vendidos = int(input("Digite o número de carros vendidos: "))

valor_vendas = float(input("Digite o valor total das vendas: "))

salario_fixo = 500.00
comissao_por_carro = 50.00
taxa_comissao = 0.05

comissao_carros = carros_vendidos * comissao_por_carro

comissao_vendas = valor_vendas * taxa_comissao

salario_total = salario_fixo + comissao_carros + comissao_vendas

print("O salário de", nome_vendedor, "é R$", salario_total)
