# https://www.urionlinejudge.com.br/judge/en/problems/view/1146

while True:
    x = int(input())
    if x == 0:
        break
    for num in range(1, x+1):
        if num == x:
            print(num)
        else:
            print(num, end=' ')
