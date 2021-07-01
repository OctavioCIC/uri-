# https://www.urionlinejudge.com.br/judge/en/problems/view/1914

n = int(input())

for _ in range(n):
    jogadas = {}
    j1, x1, j2, x2 = input().split()
    s1, s2 = map(int, input().split())
    jogadas[j1] = x1
    jogadas[j2] = x2
    for k, v in jogadas.items():
        if int(s1) + int(s2) % 2 == 0:
            if v == 'PAR':
                print(f'{jogadas[k]}')
        else:
            if v == 'IMPAR':
                print(f'{jogadas[k]}')
