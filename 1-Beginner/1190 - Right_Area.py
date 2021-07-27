posicao = int(input())

if posicao == 1:
    print("Top 1")
elif 1 < posicao <= 3:
    print("Top 3")
elif 3 < posicao <= 5:
    print("Top 5")
elif 5 < posicao <= 10:
    print("Top 10")
elif 10 < posicao <= 25:
    print("Top 25")
elif 25 < posicao <= 50:
    print("Top 50")
else:
    print("Top 100")