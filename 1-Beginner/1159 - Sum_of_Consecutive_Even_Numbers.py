# https://www.urionlinejudge.com.br/judge/en/problems/view/1159

while True:
    x = int(input())
    if x == 0:
        break
    else:
        tot = 0
        ate = x + (5*2)
        if x % 2 == 0:
            for i in range(x, ate, 2):
                    tot += i
        else:
            for i in range(x+1, ate, 2):
                    tot += i
        print(tot)
    