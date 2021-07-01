# https://www.urionlinejudge.com.br/judge/en/problems/view/1098

i = 0
j = 1
k = 0
while i <= 2:
    while k < 3:
        print (f"I={i} J={j}")
        j = j + 1
        k = k + 1
    i = i + 0.2
    if i / 10 == 0.1 or i / 10 == 0.2 :
        i = int (i)
    else:
        i = "{:.1f}".format (i)
        i = float (i)
    j = j - 3 + 0.2
    j = "{:.1f}".format (j)
    if j == "2.0" or j == "3.0" or j == "4.0" or j == "5.0":
        j = int (float (j))
    else:
        j = float (j)
    k = 0
