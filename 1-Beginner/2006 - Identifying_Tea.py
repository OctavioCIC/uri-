# https://www.urionlinejudge.com.br/judge/en/problems/view/2006

tipo = int(input())
sabores = [int(x) for x in input().split()]

print(f'{sabores.count(tipo)}')
