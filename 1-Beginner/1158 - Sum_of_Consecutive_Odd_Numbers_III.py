# https://www.urionlinejudge.com.br/judge/en/problems/view/1158

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    ate = x + (y*2)
    tot = 0
    if x % 2 == 0:
        for i in range(x+1, ate, 2):
                tot += i
    else:
        for i in range(x, ate, 2):
                tot += i
    print(tot)
    