# https://www.urionlinejudge.com.br/judge/en/problems/view/1012

a, b, c = map(float, input().split())

aTr = a * c / 2
print(f'TRIANGULO: {aTr:.3f}') # area * altura / 2
aC = 3.14159 * (c**2)
print(f'CIRCULO: {aC:.3f}') # pi * r **2
aT = ((a + b) / 2) * c
print(f'TRAPEZIO: {aT:.3f}') # base * Base / 2 * h
aQ = b * b
print(f'QUADRADO: {aQ:.3f}') # lado * lado
aR = a * b
print(f'RETANGULO: {aR:.3f}') # base * altura
