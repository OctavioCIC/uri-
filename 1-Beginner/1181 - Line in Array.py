# https://www.urionlinejudge.com.br/judge/en/problems/view/1181

matriz = [[] for _ in range(12)]

num_linha = int(input())
operacao = input()
for linha in matriz:
    for _ in range(12):
        linha.append(float(input()))
total = sum(matriz[num_linha-1])
if operacao == 'M':
    total /=12
print(f'{total:.1f}') 
