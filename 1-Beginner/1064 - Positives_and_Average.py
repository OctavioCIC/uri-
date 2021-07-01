# https://www.urionlinejudge.com.br/judge/en/problems/view/1064

valPositives = []
for _ in range(6):
    n = float(input())
    if n > 0:
        valPositives.append(n)

tot = sum(valPositives) / len(valPositives)
print(f'{len(valPositives)} valores positivos')
print(f'{tot:.1f}')
