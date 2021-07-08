# https://www.urionlinejudge.com.br/judge/en/problems/view/1914

for _ in range(int(input())):
    duo = input().split()
    tot = [int(x) for x in input().split()]
    if sum(tot) % 2 == 0:
        pos = duo.index('PAR')
        print(duo[pos-1])
    else:
        pos = duo.index('IMPAR')
        print(duo[pos-1])
