# 8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e
# exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
# valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
# informado ao usuário e o programa termina.

def calcular_media(nota1, nota2):
    if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
        media = (nota1 + nota2) / 2
        return media
    else:
        print("Nota inválida! As notas devem estar entre 0.0 e 10.0.")
        return None

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = calcular_media(nota1, nota2)
    if media is not None:
        print("A média das notas é:", media)

if __name__ == "__main__":
    main()
