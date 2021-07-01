# https://www.urionlinejudge.com.br/judge/en/problems/view/1070

a = int (input())

if a%2 == 0:
    a = a + 1
    t = 0
    while t < 6:
        print (a)
        a = a + 2
        t = t + 1
else:
    t = 0
    while t < 6:
        print (a)
        a = a + 2
        t = t + 1