m = b = 0

def loucura ():
    print ('novo calculo (1-sim 2-nao)')
    a = int(input())
    if a == 1:
         t = 0
    elif a == 2:
         t = 1
    else:
        t = loucura ()
    return t

while True:
    a = float(input())
    if a < 0 or a > 10:
        print ('nota invalida')
    else:
        m += a
        b += 1
    if b == 2:
        b  = 0
        m = "{:.2f}".format(m/2)
        print (f'media = {m}')
        if loucura () == 1:
            break
        m = 0