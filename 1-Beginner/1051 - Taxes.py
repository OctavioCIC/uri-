# https://www.urionlinejudge.com.br/judge/en/problems/view/1051

a = float (input())

if a <= 2000:
    print ("Isento")
elif 2000 < a <= 3000:
    b = a - 2000
    b = (b/100)* 8
    b = "{:.2f}".format (b)
    print (f"R$ {b}")
elif 3000 < a <= 4500:
    b = a - 3000
    b = (b/100)*18 + 80
    b = "{:.2f}".format (b)
    print (f"R$ {b}")
else:
    b = a - 4500
    b = (b/100)*28 + 80 + 270
    b = "{:.2f}".format (b)
    print (f"R$ {b}")
    