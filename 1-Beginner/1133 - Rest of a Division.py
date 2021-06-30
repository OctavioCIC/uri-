a = int(input())
b = int(input())

if a < b:
    for i in range(b-a-1):
        a += 1
        if a%5 == 2 or a%5 == 3:
            print (a)
elif a > b:
    for i in range(a-b-2):
        b += 1
        if b%5 == 2 or b%5 == 3:
            print (b)
else:
    a = b