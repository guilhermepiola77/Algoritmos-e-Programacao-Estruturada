# 30. Faça um programa que leia o valor da hora de trabalho em reais e número de horas
# trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
# o valor calculado.

valor_por_hora = float(input("Digite o valor da hora de trabalho em reais: "))

horas_trabalhadas = float(input("Digite o nùmero de horas trabalhadas no mês: "))

salario = (valor_por_hora * horas_trabalhadas)
salario_com_acrescimo = (salario * 1.10)

print("O valor a ser pago ao funcionário é R$", salario_com_acrescimo)
