# https://www.urionlinejudge.com.br/judge/en/problems/view/1175

a = []
for _ in range(20):
    x = int(input())
    a.insert(0, x)

print(a)
for pos, v in enumerate(a):
    print(f'N[{pos}] = {v}')
