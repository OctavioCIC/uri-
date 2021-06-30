a = int (input())

t = 0
c = 0
r = 0
s = 0
while t < a:
    b = input().split()
    if b[1] == 'C':
        ct = int (b[0])
        c = c + ct
    elif b[1] == 'R':
        ct = int (b[0])
        r = r + ct
    else:
        ct = int (b[0])
        s = s + ct
    t = t + 1
print (f"Total: {c + r + s} cobaias")
print (f"Total de coelhos: {c}")
print (f"Total de ratos: {r}")
print (f"Total de sapos: {s}")
print (f"Percentual de coelhos: {'{:.2f}'.format((c*100)/(c+r+s))} %")
print (f"Percentual de ratos: {'{:.2f}'.format((r*100)/(c+r+s))} %")
print (f"Percentual de sapos: {'{:.2f}'.format((s*100)/(c+r+s))} %")