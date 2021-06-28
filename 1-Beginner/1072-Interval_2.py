# https://www.urionlinejudge.com.br/judge/en/problems/view/1072

n = int(input())
dentro = 0
fora = 0

for _ in range(n):
    val = int(input())
    if val >= 10 and val <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')
