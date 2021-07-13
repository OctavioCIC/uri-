# https://www.urionlinejudge.com.br/judge/en/problems/view/1963

valI, valF = (float(x) for x in input().split())
tot = ((valF - valI)*100)/valI
print(f'{tot:.2f}%')
