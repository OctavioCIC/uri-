# https://www.urionlinejudge.com.br/judge/en/problems/view/1185

matriz = [[] for _ in range(12)]
operacao = input()
contador = 11
total = 0
tam = 0
for linha in matriz:
    for _ in range(12):
        pos = float(input())
        linha.append(pos)
        parte_linha = linha[:contador]
    if contador > 0:
        soma_linha = sum(parte_linha)
        tam += len(parte_linha)
        total += soma_linha
    contador -= 1
if operacao == 'M':
    total /= tam
print(f'{total:.1f}')
