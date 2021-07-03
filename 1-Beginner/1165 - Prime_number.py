# https://www.urionlinejudge.com.br/judge/en/problems/view/1165

def isPrime(n):
    tot = 0
    for c in range(1, n+1):
        if n % c == 0:
            tot += 1
        if tot > 2:
            return f'{n} nao eh primo'
    return f'{n} eh primo'

t = int(input())
for _ in range(t):
    x = int(input())
    print(isPrime(x))
 
