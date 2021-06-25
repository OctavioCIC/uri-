# https://www.urionlinejudge.com.br/judge/en/problems/view/1010


tot = 0
for _ in range(2):
    x = input().split()
    tot += int(x[1])*float(x[2]) 

print(f'VALOR A PAGAR: R$ {tot:.2f}')
