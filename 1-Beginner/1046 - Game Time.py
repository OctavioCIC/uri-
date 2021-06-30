a, b = (int (x) for x in input().split())

if a > b:
    r = (24-a)+ b
    print (f"O JOGO DUROU {r} HORA(S)")
elif b > a:
    r = b - a
    print (f"O JOGO DUROU {r} HORA(S)")
else:
    print ("O JOGO DUROU 24 HORA(S)")