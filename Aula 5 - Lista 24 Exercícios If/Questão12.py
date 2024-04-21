# 12. Faça um algoritmo que calcule a média ponderada das notas de 2 provas. A primeira
# prova tem peso 1 e a segunda tem peso 2. Ao final, mostrar a média do aluno e indicar
# se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual o superior
# a 70 pontos.

def calcular_media_ponderada(nota1, nota2):
    media = (nota1 * 1 + nota2 * 2) / 3
    return media

def verificar_aprovacao(media):
    if media >= 70:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))

    media = calcular_media_ponderada(nota1, nota2)
    situacao = verificar_aprovacao(media)

    print("Média do aluno:", media)
    print("Situação:", situacao)

if __name__ == "__main__":
    main()
