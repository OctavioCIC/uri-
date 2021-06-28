# https://www.urionlinejudge.com.br/judge/en/problems/view/1065

even = 0
for _ in range(5):
    n = int(input())
    if n < 0:
        n *= -1
    if n % 2 == 0:
        even += 1

print(f'{even} valores pares')

