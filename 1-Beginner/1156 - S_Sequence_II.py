# https://www.urionlinejudge.com.br/judge/en/problems/view/1156

s = 1
den = 2
for num in range(3, 40, 2):
    s += (num/den)
    den *= 2
print(f'{s:.2f}')
