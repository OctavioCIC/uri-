# https://www.urionlinejudge.com.br/judge/en/problems/view/1019


n = int(input())

horas = n // 3600
segundos = int(n % 3600)
minutos = segundos // 60
segundos = int(segundos % 60)

print(f'{horas}:{minutos}:{segundos}')