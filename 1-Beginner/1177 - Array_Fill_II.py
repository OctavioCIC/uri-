# https://www.urionlinejudge.com.br/judge/en/problems/view/1177

t = int(input())
a = list(range(t))

for pos in range(1000):
   print(f'N[{pos}] = {a[0]}')
   aux = a.pop(0)
   a.append(aux)
