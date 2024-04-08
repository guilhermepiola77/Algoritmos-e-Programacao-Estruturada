# 33. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
# subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para
# atingir seu objetivo.

altura_degrau = float(input("Digite a altura do degrau da escada (em metros): "))

altura_desejada = float(input("Digite a altura que o usuário deseja alcançar (em metros): "))

num_degraus = (altura_desejada / altura_degrau)
num_degraus = round(num_degraus + 0.5)

print("O usuário deverá subir", num_degraus, "Degraus para a atingir a altura desejada.")


