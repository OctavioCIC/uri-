x = y= 1
while x != 0 or y != 0:
    x, y = (int(x) for x in input().split())
    if y > 0 < x:
        print ('primeiro')
    elif y > 0 > x:
        print ('segundo')
    elif y < 0 > x:
        print ('terceiro')
    elif y < 0 < x:
        print ('quarto')