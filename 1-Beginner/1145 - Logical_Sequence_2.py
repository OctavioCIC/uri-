# https://www.urionlinejudge.com.br/judge/en/problems/view/1145

num, totNum = (int(x) for x in input().split())

cont = 1
for i in range(1, totNum+1):  
    if cont == num:
        print(i)
        cont = 0
    else:
        print(i, end=' ')  
    cont += 1
