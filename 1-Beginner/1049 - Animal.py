# https://www.urionlinejudge.com.br/judge/en/problems/view/1049

vertebrado = {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'}, 
'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}}

invertebrado = {'inseto': {'hematofago':'pulga', 'herbivoro': 'lagarta'}, 
'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}

a = input()
b = input()
c = input()

if a == 'vertebrado':
  for k, v in vertebrado[b].items():
    if k == c:
      print(v)
else:
  for k, v in invertebrado[b].items():
    if k == c:
      print(v)
