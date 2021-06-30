n = int (input())

t = 0
l = []
while t < n:
    a,b,c = (float(x) for x in input().split())
    media = ((a * 2) + (b * 3) + (c * 5))/ 10
    media = "{:.1f}".format(media)
    l.append (media)
    t = t + 1

t = 0
while t < n:
    print (l[t])
    t = t + 1