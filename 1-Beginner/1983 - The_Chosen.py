# https://www.urionlinejudge.com.br/judge/en/problems/view/1983

n = int(input())
maior = 0
msg = 'Minimum note not reached'
for _ in range(n):
    alunos, nota = (float(x) for x in input().split())
    if nota >= 8:
        if nota > maior:
            maior = nota
            msg = int(alunos)
print(msg)
