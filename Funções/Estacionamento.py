# Desenvolva uma aplicação Python que utilize ao menos 2 coleções e funções,
# para que seja possível realizar o cadastro de veículos em um estacionamento com o seguinte menu:

# 1 - Estacionar veículo
# 2 - Retirar veículo
# 3 - Veículos estacionados
# 4 - Está estacionado?

# 0 - Sair

# Deve gravar a placa do veículo que será a chave, marca, modelo, cor e proprietário.

def exibir_menu():
    print("\nMenu do Estacionamento")
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")

def estacionar_veiculo(veiculos_estacionados):
    placa = input("Digite a placa do veículo: ").upper()
    if placa in veiculos_estacionados:
        print("Veículo já está estacionado.")
    else:
        veiculo = {
            "marca": input("Digite a marca do veículo: "),
            "modelo": input("Digite o modelo do veículo: "),
            "cor": input("Digite a cor do veículo: "),
            "proprietario": input("Digite o nome do proprietário: ")
        }
        veiculos_estacionados[placa] = veiculo
        print("Veículo estacionado com sucesso.")

def retirar_veiculo(veiculos_estacionados):
    placa = input("Digite a placa do veículo a ser retirado: ").upper()
    if placa in veiculos_estacionados:
        del veiculos_estacionados[placa]
        print("Veículo retirado com sucesso.")
    else:
        print("Veículo não encontrado.")

def listar_veiculos_estacionados(veiculos_estacionados):
    if veiculos_estacionados:
        print("\nVeículos Estacionados:")
        for placa, veiculo in veiculos_estacionados.items():
            print(f"Placa: {placa}, Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Cor: {veiculo['cor']}, Proprietário: {veiculo['proprietario']}")
    else:
        print("Não há veículos estacionados.")

def verificar_veiculo_estacionado(veiculos_estacionados):
    placa = input("Digite a placa do veículo: ").upper()
    if placa in veiculos_estacionados:
        veiculo = veiculos_estacionados[placa]
        print(f"Veículo está estacionado. Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Cor: {veiculo['cor']}, Proprietário: {veiculo['proprietario']}")
    else:
        print("Veículo não está estacionado.")

def main():
    veiculos_estacionados = {}

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            estacionar_veiculo(veiculos_estacionados)
        elif opcao == '2':
            retirar_veiculo(veiculos_estacionados)
        elif opcao == '3':
            listar_veiculos_estacionados(veiculos_estacionados)
        elif opcao == '4':
            verificar_veiculo_estacionado(veiculos_estacionados)
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "_main_":
    main()