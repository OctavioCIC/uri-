a = m = 0
while a != 2:
    b = float(input())
    if b < 0 or b > 10:
        print ('nota invalida')
    else:
        a += 1
        m += b
print (f'media = {m/2}')