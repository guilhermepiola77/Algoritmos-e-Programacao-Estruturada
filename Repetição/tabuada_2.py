# Agora faça a tabuada do 
# 1 até a do 95, indo cada uma do 
# 1 ao 10, com no máximo mais 1 linha 
# de código.

for tabuada in range(1, 96):
    print(f"=;= tabuada DO {tabuada} =;=")
    for mult in range(1, 11):
        print(f'{mult} x {tabuada} = {mult * tabuada}')
print("=====================")

