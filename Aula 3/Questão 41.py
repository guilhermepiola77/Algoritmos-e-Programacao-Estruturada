# 41. Faça um programa para ler as dimensões de um terreno (comprimento e largura), com
# como o preço do metro de tela. Imprima o custo para cercar este mesmo terreno com
# tela.

comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite a largura do terreno em metros: "))

preco_metro_tela = float(input("Digite o preço do metro de tela em reais: "))

perimetro = 2 * (comprimento + largura)

custo_total = perimetro * preco_metro_tela

print("O custo para cercar o terreno com tela é de R$", custo_total)
