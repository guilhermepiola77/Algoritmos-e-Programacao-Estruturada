# 38. Faça um programa que leia o horário (hora, minuto e segundo) do início e a duração
# em segundo, de uma experiência atômica bélica. O programa deve resultar com o
# novo horário (hora, minuto e segundo) do término da mesma.

hora_inicio = int(input("Digite a hora de início da experiência: "))
minuto_inicio = int(input("Digite o minuto de início da experiência: "))
segundo_inicio = int(input("Digite o segundo de início da experiência: "))

duracao_segundos = int(input("Digite a duração da experiência em segundos: "))

total_segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio

total_segundos_termino = total_segundos_inicio + duracao_segundos

hora_termino = total_segundos_termino // 3600
minuto_termino = (total_segundos_termino % 3600) // 60
segundo_termino = total_segundos_termino % 60

print("Horário de término da experiência:", hora_termino, "hora(s),", minuto_termino, "minuto(s) e", segundo_termino, "segundo(s).")
