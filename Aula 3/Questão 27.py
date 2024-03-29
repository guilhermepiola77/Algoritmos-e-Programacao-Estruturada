# 27. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo
# que ele recebeu um monstruoso aumento de 1.77%.

salario_antigo = float(input("Digite o salário do funcionário: "))

aumento = salario_antigo * 0.0177
novo_salario = salario_antigo + aumento 

print("O novo salário do funcionário é: ",novo_salario)
