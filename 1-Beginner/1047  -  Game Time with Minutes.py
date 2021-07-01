a, b, c , d = (int (x) for x in input().split())

if a < c:
    if b > d:
        print (f"O JOGO DUROU {(c-a)-1} HORA(S) E {(d - b)+ 60} MINUTO(S)")
    else:
        print (f"O JOGO DUROU {c-a} HORA(S) E {d - b} MINUTO(S)")
elif a > c:
    if b > d:
        print (f"O JOGO DUROU {((c-a)-1)+ 24} HORA(S) E {(d - b)+ 60} MINUTO(S)")
    else:
        print (f"O JOGO DUROU {(c-a)+ 24} HORA(S) E {(d - b)} MINUTO(S)")
elif a == c and b != d:
    if b > d:
        print (f"O JOGO DUROU {((c-a)-1)+ 24} HORA(S) E {(d - b)+ 60} MINUTO(S)")
    else:
        print (f"O JOGO DUROU 0 HORA(S) E {(d - b)} MINUTO(S)")
else:
    print ("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")