a = int (input())
b = int (input())

soma = 0
if a < b:
    if a%2 == 0:
        soma = a - 1
        while a < b:
            a = a + 2
            soma = soma + a
    else:
        while a < b:
            a = a + 2
            soma = soma + a
if a > b:
    if b%2 == 0:
        b = b - 1
        while a > b:
            b = b + 2
            soma = soma + b
    else:
        while a > b:
            b = b + 2
            soma = soma + b
print (soma - b)
