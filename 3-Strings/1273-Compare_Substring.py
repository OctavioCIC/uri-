'https://www.urionlinejudge.com.br/judge/en/problems/view/1273'

while True:
    n = int(input())
    
    if n == 0:
        break
   
    nomes = []
    maior = 0
    
    for _ in range(n):
        nomes.append(str(input()).rstrip().lstrip())
        if len(nomes[-1]) > maior:
            maior = len(nomes[-1])
    
    for nome in nomes:
        print(f'{nome:>{maior}}')
    print()
