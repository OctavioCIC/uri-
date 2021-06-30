x, y = (float (x) for x in input().split())

if x > 0 < y:
    print ("Q1")
elif x < 0 < y:
    print ("Q2")
elif x < 0 > y:
    print ("Q3")
elif x > 0 > y:
    print ("Q4")
elif x == 0 and y == 0:
    print ("Origem")
elif x == 0:
    print ("Eixo Y")
elif y == 0:
    print ("Eixo X")