# https://www.urionlinejudge.com.br/judge/en/problems/view/1101

while True:
    s = 0
    m,n = (int (x) for x in input().split())
    if m <= 0 or n <= 0:
        break
    elif m < n:
        while m <= n:
            print (m, end=" ")
            s = s + m
            m += 1
        print (f"Sum={s}")
    elif n < m:
        while n <= m:
            print (n, end=" ")
            s = s + n
            n += 1
        print (f"Sum={s}")
    else:
        print (f"{m} Sum= {m}")
