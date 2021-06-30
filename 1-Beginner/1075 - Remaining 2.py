a = int (input())

t = 0
while t <= 10000:
    r = t%a
    if r == 2:
        print (t)
    t = t + 1