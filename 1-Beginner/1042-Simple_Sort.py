# https://www.urionlinejudge.com.br/judge/en/problems/view/1042

val = [int(x) for x in input().split()]
valSort = sorted(val)
valSort += val

cont = 0
while len(valSort) > 0:
  print(valSort.pop(0))
  if cont == 2:
    print()
  cont += 1
  