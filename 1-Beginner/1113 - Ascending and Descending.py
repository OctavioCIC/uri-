a = 0
b = 1
while a != b:
    a, b = (int (x) for x in input().split())
    if a > b:
        print ("Decrescente")
    elif a < b:
        print ("Crescente")