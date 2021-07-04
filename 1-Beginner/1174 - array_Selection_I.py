# https://www.urionlinejudge.com.br/judge/en/problems/view/1174

a = []
pos = 0
for _ in range(100):
    x = float(input())
    a.append(x) 
    if x <= 10:
        print(f'A[{pos}] = {x:.1f}')
    pos += 1
