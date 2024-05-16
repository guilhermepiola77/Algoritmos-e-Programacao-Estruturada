
for tabuada in range(1, 180):
    if tabuada % 2 == 0:
         continue
    if tabuada == 11:
            break
    print(f"=;= TABUADA DO {tabuada} =;=")
    for mult in range(1, 11):
        if mult % 2 == 0:
            continue
        print(f'{mult} x {tabuada} = {mult * tabuada}')
    print("===================")

print("ACABOU")
