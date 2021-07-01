a, b, c = (float (x) for x in input().split())

if a + b > c and b + c > a and c + a > b:
    perimetro = a + b + c
    perimetro = "{:.1f}".format (perimetro)
    print (f"Perimetro = {perimetro}")
else:
    area = ((a + b) / 2) * c
    area = "{:.1f}".format (area)
    print (f"Area = {area}")