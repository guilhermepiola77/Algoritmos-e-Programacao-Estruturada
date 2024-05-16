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


            
            #                             Conclusão
            # Primeiramente foi utilizado o "while true", que permite ao usuário uma escolha
            # até a opção de sair.

            # Em seguida é pedido para o usuário escolher uma das 4 operações matemáticas.

            # Utilizado "match opcao.uper" para que independente que o usuário escreva, saia em maiusculas
            # a escrita todas as vezes.

            # Utilizado "soma = 0.0 para que a soma seja iniciada apartir do 0."

            # Em seguida é solicitado ao usuário digitar um número ou P para parar, caso o usuário
            # utilize o P, sairá do loop.

            # Soma += serve para mostrar o resultado da "soma", serve para as outras operações também,
            # exceto a de subtração, invez do 0.0, utilizei o none, pois estava utilizando o também
            # e o resultado da subtração estava dando como um resultado da "soma" porém negativo,
            # exemplo: 5-5 = -10, alterei para none, pois é utilizado para variaveis sem valor 
            # atribuido.

            # E na operaçao de divisão foi utilizado o "if" == 0.0, que se o usuário utilizar 
            # 0 para a operação, um erro avisará que não é possivel realizar a divisão e assim
            # retornado para a tela inicial novamente.

            # Utilizado "break e continue" em cada case, seguindo o mesmo fundamento para todos.

            # No final da linha de código, utilizado o case "X", para que se usuário digitar o "X"
            # irá sair do loop principal e encerrando o programa, no caso o "break".

            # Utilizado "case _", se o usuário digitar alguma opção que seja inválida, irá exibir
            # uma mensagem de erro. 



        


        