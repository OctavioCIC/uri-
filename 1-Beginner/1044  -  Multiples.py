a, b = (int (x) for x in input().split())

if a >= b and a % b == 0:
    print ("Sao Multiplos")
elif b > a and b % a == 0:
    print ("Sao Multiplos")
else:
    print ("Nao sao Multiplos")