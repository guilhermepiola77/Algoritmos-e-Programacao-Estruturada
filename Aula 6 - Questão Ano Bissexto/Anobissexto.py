# Desenvolva um programa em Python que determine se um determinado ano é bissexto ou não, levando em 
# consideração as regras do calendário
# gregoriano. Além disso, seu programa deve fornecer uma explicação detalhada do motivo pelo qual o 
# ano é ou não é bissexto, com base nas seguintes condições:

# Um ano é bissexto se for divisível por 4, exceto quando também for divisível por 100, a menos que 
# seja divisível por 400.
# Caso o ano seja bissexto, deve-se explicar que ele possui 366 dias.
# Se o ano não for bissexto, deve-se explicar que ele possui 365 dias.
# O programa deve solicitar ao usuário que insira o ano desejado e, em seguida, fornecer a resposta
# juntamente com a explicação correspondente.

def verifica_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def main():
    print("Este programa verifica se um ano é bissexto ou não.")
    ano = int(input("Por favor, insira o ano desejado: "))

    if verifica_bissexto(ano):
        print(f"O ano {ano} é bissexto, pois atende às condições estabelecidas.")
        print("Ele possui 366 dias.")
    else:
        print(f"O ano {ano} não é bissexto, pois não atende às condições estabelecidas.")
        print("Ele possui 365 dias.")

if __name__ == "__main__":
    main()
