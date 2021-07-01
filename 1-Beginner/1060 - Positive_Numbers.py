# https://www.urionlinejudge.com.br/judge/en/problems/view/1060

cont = 0
for _ in range(6):
    num = float(input())
    if num > 0:
        cont += 1
print(f'{cont} valores positivos')
