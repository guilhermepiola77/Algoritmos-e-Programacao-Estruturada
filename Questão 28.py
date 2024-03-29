# 28. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
# Sendo que da quantia total:
# a. O primeiro ganhador receberá 46%;
# b. O segundo receberá 32%;
# c. O terceiro receberá o restante;

importancia_total = 78000000

primeiro_ganhador = (importancia_total * 0.46)
segundo_ganhador = (importancia_total * 0.32)
terceiro_ganhador = (importancia_total - primeiro_ganhador - segundo_ganhador)

print("Parcela do primeiro ganhador", primeiro_ganhador)
print("Parcela do segundo ganhador", segundo_ganhador)
print("Parcela do terceiro ganhador", terceiro_ganhador)
