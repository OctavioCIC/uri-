# https://www.urionlinejudge.com.br/judge/en/problems/view/1985

produtos = {1001:1.5, 1002:2.5, 1003:3.5, 
        1004:4.5, 1005:5.5}

val = 0
for _ in range(int(input())):
    prod, quant = (int(x) for x in input().split())
    tot = produtos[prod] * quant
    val += tot
print(f'{val:.2f}')
