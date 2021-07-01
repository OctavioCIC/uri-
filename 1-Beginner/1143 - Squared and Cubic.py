# https://www.urionlinejudge.com.br/judge/en/problems/view/1143

a = int(input())

for b in range (a):
    l = b + 1
    g = l
    for k in range (2):
        print (g, end=" ")
        g = l * g
    print (g, end="")
    if b != a:
        print ('\n', end="")
