# https://www.urionlinejudge.com.br/judge/en/problems/view/2172

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    print(n*m)
