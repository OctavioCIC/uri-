l1, l2, l3 = (float(x) for x in input().split())

if l1 < l2 or l2 < l3:
    a = max(l1, l2, l3)
    c = min(l1, l2, l3)
    b = (l1 * l2 * l3) / (a * c)
else:
    a = l1
    b = l2
    c = l3

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a ** 2 == b ** 2 + c ** 2:
    print("TRIANGULO RETANGULO")
elif a ** 2 > b ** 2 + c ** 2:
    print("TRIANGULO OBTUSANGULO")
elif a ** 2 < b ** 2 + c ** 2:
    print("TRIANGULO ACUTANGULO")

if a == b and b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
    print("TRIANGULO ISOSCELES")