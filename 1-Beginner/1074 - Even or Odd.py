# https://www.urionlinejudge.com.br/judge/en/problems/view/1074

a = int (input())

t = 0
l = []
while t < a:
    b = int (input())
    if b > 0:
        if b%2 == 0:
            l.append ("EVEN POSITIVE")
            t = t + 1
        else:
            l.append ("ODD POSITIVE")
            t = t + 1
    elif b < 0:
        if b%2 == 0:
            l.append ("EVEN NEGATIVE")
            t = t + 1
        else:
            l.append ("ODD NEGATIVE")
            t = t + 1
    else:
        l.append ("NULL")
        t = t + 1
t = 0
while t < a:
    print (l[t])
    t = t + 1
    