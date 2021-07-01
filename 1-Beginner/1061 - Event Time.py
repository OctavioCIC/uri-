# https://www.urionlinejudge.com.br/judge/en/problems/view/1061

dia1 = input().split()
h1, m1, s1 = (int(x) for x in input().split(':'))
dia2 = input().split()
h2, m2, s2 = (int(x) for x in input().split(':'))

h3 = h2 - h1
m3 = m2 - m1
s3 = s2 - s1

dia = int(dia2[1]) - int(dia1[1])
if h3 < 0 or m3 < 0 or s3 < 0:
    dia -= 1
print(f'{dia} dia(s)')

if m3 < 0:
    h3 -= 1
    print (f'{24+(h3)} hora(s)')
else:
    if h3 < 0:
        print (f'{24+(h3)} hora(s)')
    else:
        print (f'{h3} hora(s)')

if s3 < 0:
    m3 -= 1
    print (f'{60 +(m3)} minuto(s)')
    print (f'{60+(s3)} segundo(s)')
else:
    if m3 < 0:
        print (f'{60 +(m3)} minuto(s)')
        print (f'{s3} segundo(s)')
    else:
        print (f'{m3} minuto(s)')
        print (f'{s3} segundo(s)')
        