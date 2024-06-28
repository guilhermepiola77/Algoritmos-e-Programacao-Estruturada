# Desenvolver uma aplicação em Python para gerenciar uma lista de alunos, suas notas de B1 e B2,
# e realizar diversas operações através de um menu interativo. A aplicação deve permitir adicionar, 
# listar, remover, procurar alunos, calcular médias e exibir um diário da turma com formatação
# específica. Após desenvolver a aplicação, o código deve ser enviado em um repositório público 
# no GitHub.

alunos = []

def exibir_menu():
    print("Menu Interativo:")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Procurar aluno pelo RA")
    print("5 - Listar alunos aprovados")
    print("6 - Listar alunos reprovados")
    print("7 - Procurar aluno pelo nome")
    print("8 - Média da turma B1")
    print("9 - Média da turma B2")
    print("10 - Média da turma geral")
    print("11 - Diário da turma")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")
    return escolha

def adicionar_aluno():
    ra = input("Digite o RA do aluno (5 caracteres): ")
    nome = input("Digite o nome do aluno (até 27 caracteres): ")
    nota_b1 = float(input("Digite a nota da B1 (de 0 a 10): "))
    nota_b2 = float(input("Digite a nota da B2 (de 0 a 10): "))

    if nota_b1 < 0 or nota_b1 > 10 or nota_b2 < 0 or nota_b2 > 10:
        print("Notas devem estar entre 0 e 10.")
        return

    alunos.append({
        'ra': ra,
        'nome': nome,
        'nota_b1': nota_b1,
        'nota_b2': nota_b2
    })
    print("Aluno adicionado com sucesso.")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("Lista de alunos:")
    for aluno in alunos:
        print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}")

def remover_aluno():
    ra = input("Digite o RA do aluno que deseja remover: ")
    for aluno in alunos[:]:
        if aluno['ra'] == ra:
            alunos.remove(aluno)
            print(f"Aluno com RA {ra} removido.")
            return
    print(f"Aluno com RA {ra} não encontrado.")

def procurar_aluno_por_ra():
    ra = input("Digite o RA do aluno que deseja procurar: ")
    for aluno in alunos:
        if aluno['ra'] == ra:
            print(f"Aluno encontrado - RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}")
            return
    print(f"Aluno com RA {ra} não encontrado.")

def listar_aprovados():
    aprovados = [aluno for aluno in alunos if (aluno['nota_b1'] + aluno['nota_b2']) / 2 >= 7]
    if not aprovados:
        print("Nenhum aluno aprovado encontrado.")
        return

    print("Lista de alunos aprovados:")
    for aluno in aprovados:
        print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Média: {(aluno['nota_b1'] + aluno['nota_b2']) / 2}")

def listar_reprovados():
    reprovados = [aluno for aluno in alunos if (aluno['nota_b1'] + aluno['nota_b2']) / 2 < 7]
    if not reprovados:
        print("Nenhum aluno reprovado encontrado.")
        return

    print("Lista de alunos reprovados:")
    for aluno in reprovados:
        print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Média: {(aluno['nota_b1'] + aluno['nota_b2']) / 2}")

def procurar_aluno_por_nome():
    nome = input("Digite o nome do aluno que deseja procurar: ")
    encontrados = [aluno for aluno in alunos if aluno['nome'].lower() == nome.lower()]
    if not encontrados:
        print(f"Aluno com nome '{nome}' não encontrado.")
        return

    print(f"\nAluno encontrado(s) com nome '{nome}':")
    for aluno in encontrados:
        print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}")

def calcular_media_b1():
    if not alunos:
        print("Não há alunos cadastrados para calcular média.")
        return

    media_b1 = sum(aluno['nota_b1'] for aluno in alunos) / len(alunos)
    print(f"Média da turma B1: {media_b1:.2f}")

def calcular_media_b2():
    if not alunos:
        print("Não há alunos cadastrados para calcular média.")
        return

    media_b2 = sum(aluno['nota_b2'] for aluno in alunos) / len(alunos)
    print(f"Média da turma B2: {media_b2:.2f}")

def calcular_media_geral():
    if not alunos:
        print("Não há alunos cadastrados para calcular média.")
        return

    media_geral = sum((aluno['nota_b1'] + aluno['nota_b2']) / 2 for aluno in alunos) / len(alunos)
    print(f"Média geral da turma: {media_geral:.2f}")

def imprimir_diario():
    if not alunos:
        print("Não há alunos cadastrados para gerar o diário.")
        return

    print("Diário da turma:")
    print("{:<15} {:<15} {:<16} {:<60}".format("RA", "Nome", "Nota B1", "Nota B2"))
    for aluno in alunos:
        ra = aluno['ra'].ljust(15)
        nome = aluno['nome'][:13].ljust(15)
        nota_b1 = f"{aluno['nota_b1']:.2f}".rjust(6)
        nota_b2 = f"{aluno['nota_b2']:.2f}".rjust(14)
        print(f"{ra} {nome} {nota_b1} {nota_b2}")

def main():
    while True:
        escolha = exibir_menu()

        if escolha == '1':
            adicionar_aluno()
        elif escolha == '2':
            listar_alunos()
        elif escolha == '3':
            remover_aluno()
        elif escolha == '4':
            procurar_aluno_por_ra()
        elif escolha == '5':
            listar_aprovados()
        elif escolha == '6':
            listar_reprovados()
        elif escolha == '7':
            procurar_aluno_por_nome()
        elif escolha == '8':
            calcular_media_b1()
        elif escolha == '9':
            calcular_media_b2()
        elif escolha == '10':
            calcular_media_geral()
        elif escolha == '11':
            imprimir_diario()
        elif escolha == '0':
            print("Finalizando Programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


                                # Guilherme A Piola 27/06/2024

            #     O menu interage com o usuário com as seguintes opções:

            #     Adicionar aluno: adicionamos um novo aluno com RA, nome e notas das 
            #     avaliações B1 e B2.

            #     Listar alunos: Mostra todos os alunos cadastrados, exibindo ra, nome, nota B1 
            #     e nota B2.

            #     Remover aluno: Remove um aluno com base no RA listado.

            #     Procurar aluno por RA: Faz a busca e exibe um aluno específico pelo seu ra.

            #     Listar alunos aprovados: Mostra os alunos que possuem a média entre B1 e B2 é 
            #     maior ou igual a 7.

            #     Listar alunos reprovados: Mostra os alunos que possuem média entre B1 e B2 
            #     é menor que 7.

            #     Procurar aluno pelo nome: Busca e mostram os alunos pelo nome correspondente 
            #     apresentado 
            #   
            #     Média da turma B1: Faz o calculo e exibe a média das notas B1 de todos os alunos 
            #     cadastrados.

            #     Média da turma B2: Faz o calculo e exibe a média das notas B2 de todos os alunos
            #     cadastrados.

            #     Média da turma geral: Faz o calculo e exibe a média geral das notas 
            #     (média de B1 e B2) de todos os alunos cadastrados.

            #     Diário da turma: Mostra um diário exibido pelo ra, nome, nota B1 e nota B2 de 
            #     todos os alunos cadastrados.

            #     Sair: Encerra o programa.

            #     é utilizado um script para a lista chamada "alunos", sua função é armazenar
            #     os dados dos alunos, pelo RA, nome, nota b1, nota b2 e dicionário.
    
    