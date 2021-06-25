# https://www.urionlinejudge.com.br/judge/en/problems/view/1020


n = int(input())

anos = n // 365
print(anos, 'ano(s)')
aux = (n % 365) 
meses = aux // 30
print(meses, 'mes(es)')
dias = aux % 30
print(dias, 'dia(s)')
