# https://www.urionlinejudge.com.br/judge/en/problems/view/1173

n = int(input())
cont = 0
for _ in range(10):
    if cont > 0:
        n *= 2
    print(f'N[{_}] = {n}')
    cont += 1
   