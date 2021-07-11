# https://www.urionlinejudge.com.br/judge/en/problems/view/2028

caso = 1
while True:
    try:
        n = int(input())
        l = []
        for i in range(n+1):
            if i == 0:
                for j in range(i+1):
                    l.append(i)
            else:
                for j in range(i):
                    l.append(i)
        if len(l) == 1:
            print(f'Caso {caso}: 1 numero')
        else:
            print(f'Caso {caso}: {len(l)} numeros')
        print(*l)
        print()
        caso += 1        
    except EOFError:
        break
