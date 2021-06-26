# https://www.urionlinejudge.com.br/judge/en/problems/view/1036

a, b, c = map(float, input().split())

delta = b**2 - (4*a*c)

if a == 0 or delta < 0:
    print('Impossivel calcular')

else:
    r1 = (-b + (delta ** 0.5)) / (2*a)
    r2 = (-b - (delta ** 0.5)) / (2*a)
    print(f'{r1:.5f}')
    print(f'{r2:.5f}')
