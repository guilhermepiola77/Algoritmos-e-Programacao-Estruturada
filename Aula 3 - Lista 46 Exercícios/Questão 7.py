# 7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: 𝐶 = 5.0 ∗
# (𝐹−32.0)
# 9.0
# , sendo que 𝐹 a temperatura em
# Fahrenheit e 𝐶 a temperatura em Celsius.


Fahrenheit = float(input("Informe a temperatura em Celsius:"))
Celsius =  5.0 * (Fahrenheit - 32)  / 9 
print ("A temperatura em Celsius é:",Celsius)