# 32. Escreva um programa de ajuda para vendedor. A partir de um valor total lido mostre:
# a. O total a pagar com desconto de 10%;
# b. O valor de cada parcela, no parcelamento de 3x sem juros;
# c. A comissão do vendedor, caso de a venda ser a vista (5% sobre o valor com
# desconto);
# d. A comissão do vendedor, caso de a venda ser parcelada (5% sobre o valor
# total)

valor_total = float(input("Digite o valor total da venda: "))

desconto = (valor_total * 0.10)
total_com_desconto = (valor_total - desconto)
valor_parcela = (total_com_desconto / 3)
comissao_a_vista = (total_com_desconto * 0.05)
comissao_parcelada = (valor_total * 0.05)

print("a. Total a pagar com desconto de 10%:",total_com_desconto)
print("b. Valor de cada parcela (3x sem juros):",valor_parcela)
print("c. Comissão do vendedor (venda a vista):",comissao_a_vista)
print("d. Comissão do vendedor (venda parcelada):",comissao_parcelada)
