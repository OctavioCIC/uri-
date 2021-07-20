'https://www.urionlinejudge.com.br/judge/en/runs/code/23144104'
times = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'o', 'p']
cont = 0
for _ in range(15):
    m, n = map(int, input().split())
    if cont == len(times):
        cont = 0
    if m > n:
        del times[cont+1]
    else:
        del times[cont]
    cont += 1
print(times[0].upper())