# https://www.urionlinejudge.com.br/judge/en/problems/view/1142

a = int(input())
b = 0
for i in range(a):
    for k in range (3):
        b += 1
        print (b, end=" ")
    print ('PUM')
    b += 1
