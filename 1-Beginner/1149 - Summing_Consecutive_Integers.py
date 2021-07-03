# https://www.urionlinejudge.com.br/judge/en/problems/view/1149

aux = [int(x) for x in input().split()]

tot = 0
l = []
if len(aux) > 2:
    for i in aux:
        if i > 0:
            l.append(i)
else:
    l = aux
for i in range(l[0], (l[0]+l[1])):
        tot += i

print(tot)
