# 29. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que
# solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que
# deverá ser paga, sabendo-se que são descontados 11% de previdência social, e após
# isso 8% para imposto de renda.

dias_trabalhados = int(input("Digite o numero de dias trabalhados pelo encanador: "))

salario_bruto = dias_trabalhados * 30.00
previdencia = (salario_bruto * 0.11)
salario_previdencia = (salario_bruto - previdencia)
imposto_de_renda = (salario_previdencia * 0.08)
salario_liquido = (salario_previdencia - imposto_de_renda)

print("A quantia líquida a ser paga é R$ ",salario_liquido)

