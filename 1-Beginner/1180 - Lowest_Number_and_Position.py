# https://www.urionlinejudge.com.br/judge/en/problems/view/1180

n = int(input())

a = [int(x) for x in input().split()]
aux = sorted(a)
print(f'Menor valor: {aux[0]}')
print(f'Posicao: {a.index(aux[0])}')
