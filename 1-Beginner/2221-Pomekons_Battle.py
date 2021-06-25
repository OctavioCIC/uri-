# https://www.urionlinejudge.com.br/judge/en/runs/code/23197969


for _ in range(int(input())):
    bonus = int(input())
    x = input().split()
    y = input().split()
    vd = (int(x[0]) + int(x[1]))/ 2
    vg = (int(y[0]) + int(y[1]))/ 2
    if int(x[2]) % 2 == 0:
        vd += bonus
    if int(y[2]) % 2 == 0:
        vg += bonus
    
    if vd > vg:
        print('Dabriel')
    elif vg > vd:
        print('Guarte')
    else:
        print('Empate')
