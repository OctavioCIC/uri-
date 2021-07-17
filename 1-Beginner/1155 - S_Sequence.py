# https://www.urionlinejudge.com.br/judge/en/problems/view/1155

s = 1
for i in range(2, 101):
    s += (1/i)

print(f'{s:.2f}')
