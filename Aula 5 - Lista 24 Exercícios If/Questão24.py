# 24. A tarifas de certo parque de estacionamento são as seguintes:
# a. 1ª e 2ª hora – R$ 1,00 cada
# b. 3ª e 4ª hora – R$ 1,40 cada
# c. 5ª hora e seguintes R$ 2,00 cada
# O numero de horas a pagar é sempre inteiro arredondado por excesso. Deste modo,
# quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que
# pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e
# partida são apresentados na foram de pares de inteiros, representando horas e
# minutos. Por exemplo, o par 12 50 representará “dez para a uma da tarde”. Pretendese criar um programa que, lidos pelo teclado s momento de chegada e de partida,
# escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chega e a
# partida se dão com intervalor não superior a 24 horas. Portanto, se uma dada hora de
# chegada for superior à partida, isso não é uma situação de erro, antes significará que a
# partida ocorreu no dia seguinte ao da chegada.

def calcular_preco_estacionamento(chegada, partida):
    hora_chegada, minuto_chegada = chegada
    hora_partida, minuto_partida = partida

    minutos_chegada_total = hora_chegada * 60 + minuto_chegada
    minutos_partida_total = hora_partida * 60 + minuto_partida

    duracao_em_minutos = minutos_partida_total - minutos_chegada_total

    horas_estacionadas = duracao_em_minutos / 60
    horas_arredondadas = int(horas_estacionadas) + 1 if duracao_em_minutos % 60 > 0 else int(horas_estacionadas)

    if horas_arredondadas <= 2:
        preco = horas_arredondadas * 1.00
    elif 3 <= horas_arredondadas <= 4:
        preco = horas_arredondadas * 1.40
    else:
        preco = horas_arredondadas * 2.00

    return preco

def main():
    chegada = tuple(map(int, input("Digite a hora de chegada (formato hh mm): ").split()))
    partida = tuple(map(int, input("Digite a hora de partida (formato hh mm): ").split()))

    preco = calcular_preco_estacionamento(chegada, partida)
    print("O preço cobrado pelo estacionamento é: R$", preco)

if __name__ == "__main__":
    main()
