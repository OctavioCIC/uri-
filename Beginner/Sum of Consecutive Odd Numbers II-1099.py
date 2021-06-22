'https://www.urionlinejudge.com.br/judge/en/problems/view/1099'

n = int(input())
for _ in range(n):
    num = [int(x) for x in input().split()]
    num = sorted(num)
    tot = 0
    for i in range(num[0]+1, num[1]):
        if i % 2 != 0:
            tot += i
    print(tot)
