# 42. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
# porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica.
# Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos de 45%,
# prepare um algoritmo para ler o custo de fábrica do carro e imprimir o custo ao
# consumidor.

custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

porcentagem_distribuidor = 0.12
porcentagem_impostos = 0.45

valor_distribuidor = custo_fabrica * porcentagem_distribuidor

valor_impostos = custo_fabrica * porcentagem_impostos

custo_consumidor = custo_fabrica + valor_distribuidor + valor_impostos

print("O custo ao consumidor do carro é de R$", custo_consumidor)

