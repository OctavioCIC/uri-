# https://www.urionlinejudge.com.br/judge/en/problems/view/1164

def is_perfect(n):
    tot = 0
    for d in range(1, n):
        if n % d == 0:
            tot += d 
    if n == tot:
        return f'{n} eh perfeito'     
    return f'{n} nao eh perfeito'

t = int(input())
for _ in range(t):
    x = int(input())
    print(is_perfect(x))
