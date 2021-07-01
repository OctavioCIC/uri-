# https://www.urionlinejudge.com.br/judge/en/problems/view/1144

a = int(input())

for b in range (a):
    ln = []
    l = b + 1
    g = l
    for k in range (2):
        print (g, end=" ")
        ln.append(g)
        g = l * g
    print (g, end="")
    if b != a:
        print ('\n', end="")
    print (ln[0],end=' ')
    print (ln[1]+1,end=' ')
    print (g+1,end='')
    if b != a:
        print ('\n', end="")
