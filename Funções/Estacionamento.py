def mostrar_menu():
    print("Menu do Estacionamento")
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")

def estacionando_veiculo(veiculos_estacionados):
    placa = input("Digite a placa do veículo: ").upper()
    if placa in veiculos_estacionados:
        print("Veículo já está estacionado.")
        return
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    proprietario = input("Digite o nome do proprietário: ")
    
    veiculo = {
        "marca": marca,
        "modelo": modelo,
        "cor": cor,
        "proprietario": proprietario
    }
    
    veiculos_estacionados[placa] = veiculo
    print("Veículo estacionado com sucesso.")

def retirar_veiculo(veiculos_estacionados):
    placa = input("Digite a placa do veículo para retirar: ").upper()
    if placa in veiculos_estacionados:
        del veiculos_estacionados[placa]
        print("Veículo retirado com sucesso.")
    else:
        print("Veículo não encontrado.")

def mostrar_veiculos_estacionados(veiculos_estacionados):
    if not veiculos_estacionados:
        print("Não possui veículos estacionados.")
        return
    
    print("Veículos Estacionados:")
    for placa, veiculo in veiculos_estacionados.items():
        print(f"Placa: {placa}, Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Cor: {veiculo['cor']}, Proprietário: {veiculo['proprietario']}")

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
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            estacionando_veiculo(veiculos_estacionados)
        elif opcao == '2':
            retirar_veiculo(veiculos_estacionados)
        elif opcao == '3':
            mostrar_veiculos_estacionados(veiculos_estacionados)
        elif opcao == '4':
            verificar_veiculo_estacionado(veiculos_estacionados)
        elif opcao == '0':
            print("Finalizando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()




                        # Guilherme Antonio Piola, criado em 19/06/2024
    
            #     def mostrar_menu():
            # A função dela é imprimir na tela o menu do estacionamento com todas as opções 
            # numeradas abaixo dela, (Opção 1,Opção 2, Opção 3, Opção 4 e Opção 0.)
    
            
            #     def estacionando_veiculo(veiculos_estacionados):

            # Esta função permite ao usuário inserir os detalhes do veículo para estacioná-lo o veiculo.
            # Primeiro, irá solicitar a placa do veículo, se essa placa já estiver constando no dicionário 
            # veiculos_estacionados, exibirá uma mensagem informando que o veículo já está estacionado
            #  e retornará sem fazer mais nada.
            # Caso contrário, solicitara a marca, modelo, cor e nome do proprietário do veículo.
            # Cria um dicionário com essas informações e adiciona a placa como chave no dicionário 
            # 
            # (veiculos_estacionados.)
            # Imprime uma mensagem indicando que o veículo foi estacionado com sucesso.

           
            #  retirar_veiculo(veiculos_estacionados):

            # Esta função permite ao usuário informar a placa de um veículo para
            #  retirá-lo do estacionamento.
            # Solicita a placa do veículo a ser retirado.
            # Se a placa estiver no dicionário veiculos_estacionados, 
            # irá remover essa entrada (veículo) do dicionário.
            # Se não, exibe uma mensagem informando que o veículo não foi encontrado.

            
            #  mostrar_veiculos_estacionados(veiculos_estacionados):

            # Esta função verifica se a veículos estacionados no dicionário veiculos_estacionados.
            # Se o dicionário estiver vazio, imprimirá uma mensagem informando que não há veículos 
            # estacionados.
            # Caso contrário, repitirá sobre o dicionário e irá imprimir
            #  as informações de cada veículo estacionado,
            # incluindo placa, marca, modelo, cor e proprietário.

            
            # verificar_veiculo_estacionado(veiculos_estacionados):

            # A função permitirá ao usuário verificar se um veículo específico está estacionado.
            # Solicitará a placa do veículo.
            # Irá verificar se a placa está presente no dicionário veiculos_estacionados.
            # Se estiver presente, imprime na tela as informações completas do veículo 
            # (marca, modelo, cor e proprietário).
            # Caso contrário, exibirá uma mensagem informando que o veículo não está estacionado.


            # main():

            # A função principal do programa é coordenar todas as operações.
            # Inicializa um dicionário vazio veiculos_estacionados para armazenar os 
            # veículos estacionados.
            # Utilizando um loop while True para exibir o menu (mostrar_menu()), irá obter a 
            # escolha do usuário (opcao = input("Escolha uma opção: ")) e executar a 
            # função correspondente com base na escolha do usuário.
            # As opções do menu são implementadas utilizando condicionais (if, elif, else) 
            # para chamar as funções (estacionando_veiculo, retirar_veiculo, 
            # mostrar_veiculos_estacionados e verificar_veiculo_estacionado.)
            # Se o usuário escolher a opção 0, o programa exibirá a seguinte mensagem
            #  "Finalizando programa." e encerrará o loop (break).
            # Essas funções trabalham juntas para simular um sistema simples de 
            # gerenciamento de estacionamento, permitindo ao usuário adicionar, remover, 
            # listar e verificar veículos estacionados.
                        