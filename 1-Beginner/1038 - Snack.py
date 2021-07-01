# https://www.urionlinejudge.com.br/judge/en/problems/view/1038

valores = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

x, y = map(int, input().split())

tot = valores[x] * y
print(f'Total: R$ {tot:.2f}')
