# 21. Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for
# divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988,
# 1992, 1996.

def eh_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

def main():
    ano = int(input("Digite um ano para verificar se é bissexto: "))
    if eh_bissexto(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

if __name__ == "__main__":
    main()

