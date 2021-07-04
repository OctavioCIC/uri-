# https://www.urionlinejudge.com.br/judge/en/problems/view/1172

for pos in range(0, 10):
    x = int(input())
    if x <= 0:
        x = 1
    print(f'X[{pos}] = {x}')
