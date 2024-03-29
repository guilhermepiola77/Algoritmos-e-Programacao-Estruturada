# 31. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
# sabendo-se que esse funcionário em uma gratificação de 5% sobre o salário-base.
# Além disso, ele paga 7% de imposto sobre o salário-base.

salario_base = float(input("Digite o salário-base do funcionário: "))

gratificacao = (salario_base * 0.05)
imposto = (salario_base * 0.07)
salario_restante = (salario_base - imposto)
salario_final = (salario_restante + gratificacao)

print("O salário a receber é R$ ", salario_final)
