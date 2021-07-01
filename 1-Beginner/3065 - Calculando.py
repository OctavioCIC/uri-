# https://www.urionlinejudge.com.br/judge/en/problems/view/3065

while True:
    m = int(input())
    if m == 0:
        break
    conta = input()
    num = []
    sinal = []
    for i in conta:
        if i.isnumeric():
            num.append(i)
        else:
            sinal.append(i)
    soma = num.pop()
    for j in sinal:
        if j == '-':
            soma -= int(num.pop())
        else:
            soma += int(num.pop())
