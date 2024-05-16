# Desenvolva uma calculadora estilo HP.
# Irá solicitar para o usuário informar a opção
# 1 - Adição
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão
# Quando escolher uma das opções, irá receber os valores numéricos até o usuário digitar a letra P,
# posterior a isso exibirá o resultado do calculo escolhido, e voltará para o menu.

while True:
    opcao = input('Digite a opção:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nX - Sair\nOpção: ')
    
    match opcao.upper():
        case '1':
            soma = 0.0
            while True:
                num = input('Digite um número ou P para parar: ')
                if num.upper() == 'P':
                    break
                soma += float(num)  
            print(f"A soma é {soma}")
        
        case '2':
            subtracao = None
            while True:
                num = input('Digite um número ou P para parar: ')
                if num.upper() == 'P':
                    break
                if subtracao is None:
                    subtracao = float(num)
                else:
                    subtracao -= float(num)
            print(f"A subtração é {subtracao}")
        
        case '3':
            multiplicacao = 1.0
            while True:
                num = input('Digite um número ou P para parar: ')
                if num.upper() == 'P':
                    break
                multiplicacao *= float(num)  
            print(f"A multiplicação é {multiplicacao}")
        
        case '4':
            divisao = None
            while True:
                num = input('Digite um número ou P para parar: ')
                if num.upper() == 'P':
                    break
                if divisao is None:
                    divisao = float(num)
                else:
                    if float(num) == 0.0:
                        print("Erro: Divisão por zero não é permitida.")
                        continue
                    divisao /= float(num)
            print(f"A divisão é {divisao}")
        
        case 'X':
            break
            
        case _:
            print("Opção inválida, tente novamente.")