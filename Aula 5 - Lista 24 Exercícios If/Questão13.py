# 13. A nota final de um estudante é calculada a partir de três notas atribuídas entre o
# intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação
# semestral e a um exame final. A média das três notas mencionadas anteriormente
# obedece aos pesos: Trabalho de laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
# De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e
# 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações
# necessárias.

def calcular_nota_final(nota_lab, nota_semestral, nota_final):
    media = (nota_lab * 2 + nota_semestral * 3 + nota_final * 5) / 10
    return media

def verificar_situacao_aluno(media):
    if 0 <= media <= 2.9:
        return "Reprovado"
    elif 3 <= media <= 4.9:
        return "Recuperação"
    else:
        return "Aprovado"

def main():
    nota_lab = float(input("Digite a nota do trabalho de laboratório (entre 0 e 10): "))
    nota_semestral = float(input("Digite a nota da avaliação semestral (entre 0 e 10): "))
    nota_final = float(input("Digite a nota do exame final (entre 0 e 10): "))

    media = calcular_nota_final(nota_lab, nota_semestral, nota_final)
    situacao = verificar_situacao_aluno(media)

    print("Média do aluno:", media)
    print("Situação:", situacao)

if __name__ == "__main__":
    main()
