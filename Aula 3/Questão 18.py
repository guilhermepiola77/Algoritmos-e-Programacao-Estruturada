# 18. Sabendo que a formula para aprovação é: 𝐺1+(𝐺2∗2)
# 3
# ≥ 7.0, desenvolva uma aplicação
# que leia as notas de G1 e G2 e apresente a média do semestre.

nota1 = float(input("Digite a nota de G1: "))
nota2 = float(input("Digite a nota de G2: "))

média = (nota1 + nota2 * 2 ) / 3 


print("A média do semestre é: ",média)
