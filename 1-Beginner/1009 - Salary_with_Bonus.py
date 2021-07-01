# https://www.urionlinejudge.com.br/judge/en/problems/view/1009

name = input()
salary = float(input())
prod = float(input())

porc = prod * 0.15
tot = porc + salary

print(f'TOTAL = R$ {tot:.2f}')
