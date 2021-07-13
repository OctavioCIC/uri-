
ciclo = int(input())
rpm = [int(x) for x in input().split()]

queda = 0
maior = 0
for r in rpm:
    if r > maior:
        maior = r
    if r < maior:
        queda = r
        break
if queda in rpm:
    print(rpm.index(queda))
elif queda == 0:
    print(queda)
