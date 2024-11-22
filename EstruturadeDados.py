def gerar_cronograma(preco_compra):
    taxa_anual = 0.12
    pagamento_mensal_percentual = 0.05
    pagamento_inicial_percentual = 0.10

    pagamento_inicial = preco_compra * pagamento_inicial_percentual
    saldo_total = preco_compra - pagamento_inicial
    pagamento_mensal = saldo_total * pagamento_mensal_percentual
    taxa_mensal = taxa_anual / 12

    print(f"{'Mês':<5} {'Saldo Total':<15} {'Juros':<10} {'Principal':<15} "
          f"{'Pagamento':<15} {'Saldo Remanescente':<20}")
    print("=" * 75)

    mes = 1
    while saldo_total > 0:
        juros = saldo_total * taxa_mensal
        principal = pagamento_mensal - juros
        saldo_remanescente = saldo_total - principal

        if saldo_remanescente < 0:
            pagamento_mensal = saldo_total + juros
            saldo_remanescente = 0

        print(f"{mes:<5} {saldo_total:<15.2f} {juros:<10.2f} {principal:<15.2f} "
              f"{pagamento_mensal:<15.2f} {saldo_remanescente:<20.2f}")

        saldo_total = saldo_remanescente
        mes += 1

preco_compra = float(input("Digite o preço de compra do computador: R$ "))
gerar_cronograma(preco_compra)
