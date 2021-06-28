# https://www.urionlinejudge.com.br/judge/en/problems/view/1066

even = 0
odd = 0
positive = 0
negative = 0

for _ in range(5):
    n = int(input())
    if n >= 0:
        if n != 0:
            positive += 1
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        negative += 1
        n *= -1
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{positive} valor(es) positivo(s)')
print(f'{negative} valor(es) negativo(s)')
