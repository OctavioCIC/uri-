# https://www.urionlinejudge.com.br/judge/en/problems/view/1018


valor = int(input())
banco = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for v in banco:
  tot = valor // v
  valor %= v
  print(f'{tot} nota(s) de R$ {v},00')  
  