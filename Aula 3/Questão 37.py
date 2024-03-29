# 37. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

H = int(input("Qual a hora: "))
hora = H // 3600

print("a hora é: {}".format(hora,H))
minutos = int(input("Qual são os minutos: "))
hora = minutos // 3600
print("Os minutos são: {}".format(hora,minutos))
segundos = int(input("Qual os segundos "))
hora = segundos // 3600
