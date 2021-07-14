# https://www.urionlinejudge.com.br/judge/en/problems/view/1789

while True:
    try:
        tot_lesmas = int(input())
        veloc_lesmas = [int(x) for x in input().split()]
        maior_veloc = max(veloc_lesmas)
        if maior_veloc < 10:
            print('1')
        elif 10 <= maior_veloc < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break
