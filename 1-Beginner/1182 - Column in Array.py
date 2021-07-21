# https://www.urionlinejudge.com.br/judge/en/problems/view/1182

matriz = [[] for _ in range(12)]

num_linha = int(input())
operacao = input()
total = 0
for linha in matriz:
    contador = 0
    for _ in range(12):
        pos = float(input())
        linha.append(pos)
        if contador == num_linha:
            total += pos
        contador += 1 
if operacao == 'M':
    total /=12
print(f'{total:.1f}') 
