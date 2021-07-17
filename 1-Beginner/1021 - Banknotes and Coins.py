# https://www.urionlinejudge.com.br/judge/en/problems/view/1021

valor = float(input()) + 0.00001
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    totNotas = valor / nota
    valor %= nota
    print(f'{int(totNotas)} nota(s) de R$ {nota:.2f}')  

print('MOEDAS:')
for moeda in moedas:
    totMoedas = valor / moeda
    valor %= moeda
    print(f'{int(totMoedas)} moeda(s) de R$ {moeda:.2f}')
