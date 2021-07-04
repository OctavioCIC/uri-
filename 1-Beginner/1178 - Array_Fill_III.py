# https://www.urionlinejudge.com.br/judge/en/problems/view/1178

x = float(input())

for pos in range(100):
   print(f'N[{pos}] = {x:.4f}')
   x /= 2
