# https://www.urionlinejudge.com.br/judge/en/problems/view/2763

cpf = input()
for pos in cpf:
    if (pos == '.' or pos == '-'):
        print()
    else:
        print(pos,end='')
print()
