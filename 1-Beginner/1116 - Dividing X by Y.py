a = int(input())
for i in range (a):
    x, y = (int(x) for x in input().split())
    if y == 0:
        print ('divisao impossivel')
    else:
        print (x/y)