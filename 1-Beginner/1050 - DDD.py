# https://www.urionlinejudge.com.br/judge/en/problems/view/1050

destinos = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro',
32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}

ddd = int(input())

if ddd in destinos:
    print(destinos[ddd])
else:
    print('DDD nao cadastrado')
