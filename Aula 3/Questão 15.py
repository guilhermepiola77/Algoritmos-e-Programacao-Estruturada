# 15. Uma empresa de piscinas precisa saber qual o volume em que cada piscina terá em
# M³, sendo que o usuário irá informar a largura, comprimento e profundidade.

largura = float(input("Informe a largura da piscina em metros: "))
comprimento = float(input("Informe o comprimento da piscina em metros: "))
profundidade = float(input("Informe a profundidade da piscina em metros: "))

volume = largura * comprimento * profundidade 

print("O valor da piscina é:",volume, "metros cúbicos")
