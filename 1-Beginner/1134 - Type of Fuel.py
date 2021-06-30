resultado = {1:0, 2:0, 3:0}
while True:
    a = int (input())
    if a == 4:
        break
    try:
        resultado[a] += 1
    except:
        continue
print (f'''MUITO OBRIGADO
Alcool: {resultado[1]}
Gasolina: {resultado[2]}
Diesel: {resultado[3]}''')