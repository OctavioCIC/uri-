# https://www.urionlinejudge.com.br/judge/en/problems/view/1589

while True:
    try:
        reclamacoes = int(input())
        if reclamacoes == 0:
            print('Vai ter copa!')
        else:
            print('Vai ter duas!')
    except EOFError:
        break
        