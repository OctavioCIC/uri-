# https://www.urionlinejudge.com.br/judge/en/problems/view/1179

par = []
impar = []

for i in range(15):
    n = int(input()) 
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
        
    if len(par) == 5:
        for pos, valor in enumerate(par):
            print(f'par[{pos}] = {valor}')
        par.clear()
    elif len(impar) == 5:
        for pos, valor in enumerate(impar):
            print(f'impar[{pos}] = {valor}')
        impar.clear()
    else:
        if i == 14:
            for pos, valor in enumerate(impar):
                print(f'impar[{pos}] = {valor}')
            
            for pos, valor in enumerate(par):
                print(f'par[{pos}] = {valor}')

