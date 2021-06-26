# https://www.urionlinejudge.com.br/judge/en/problems/view/1035

def test(a, b, c, d):
  condicao = True
  if b <= c:
    return False
  elif d <= a:
    return False
  elif c+d <= a+b:
    return False
  elif c <= 0 and d <= 0:
    return False
  elif a % 2 != 0:
    return False
  return condicao

a, b, c, d = map(int, input().split())

x = test(a, b, c, d)

if x:
  print('Valores aceitos')
else:
  print('Valores nao aceitos')
