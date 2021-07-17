# https://www.urionlinejudge.com.br/judge/en/problems/view/1176

fib = [0,1]

for _ in range(60):
    valor = fib[-1] + fib[-2]
    fib.append(valor)
    
num = int(input())
for _ in range(num):
    n = int(input())
    print(f'Fib({n}) = {fib[n]}')
