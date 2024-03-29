# 45. Calcule a média de um aluno na disciplina de ED. Para isso solicite o nome do aluno, a
# nota da prova e a nota qualitativa. Sabe-se que a nota da prova tem peso 2 e a nota
# qualitativa peso 1. Mostre a média como resultado.

nome_aluno = input("Digite o nome do aluno: ")

nota_prova = float(input("Digite a nota da prova (de 0 a 10): "))

nota_qualitativa = float(input("Digite a nota qualitativa (de 0 a 10): "))

media = (nota_prova * 2 + nota_qualitativa * 1) / 3

print("A média do aluno", nome_aluno, "na disciplina de ED é:", media)
