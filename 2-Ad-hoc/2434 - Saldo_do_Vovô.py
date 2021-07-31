# https://www.urionlinejudge.com.br/judge/en/problems/view/2434

dias, saldo_total = map(int, input().split())
menor_saldo = 0

for i in range(dias):
    deposito = int(input())
    saldo_total += deposito
    if i == 0:
        menor_saldo = saldo_total
    if saldo_total < menor_saldo:
        menor_saldo = saldo_total

print(menor_saldo)
