# https://www.urionlinejudge.com.br/judge/en/problems/view/1154

media = 0
cont = 0
while True:
    n = int(input())
    if n < 0:
        break
    media += n
    cont += 1
    
print(f'{media/(cont):.2f}')
