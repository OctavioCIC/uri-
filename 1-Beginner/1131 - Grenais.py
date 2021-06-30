e = g = i = o = 0
while o != 2:
    I, G = (int (x) for x in input().split())
    if G > I:
        g += 1
    elif I > G:
        i += 1
    else:
        e += 1
    print ('Novo grenal (1-sim 2-nao)')
    o = int(input())
print (f'{g+i+e} grenais\nInter:{i}\nGremio:{g}\nEmpates:{e}')
if i > g:
    print ('Inter venceu mais')
elif g > i:
    print ('Gremio venceu mais')
else:
    print ('Nao houve vencedor')