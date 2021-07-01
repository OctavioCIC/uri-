'https://www.urionlinejudge.com.br/judge/en/problems/view/1168'

leds = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}

for _ in range(int(input())):
    total = 0
    led = input()
    for i in led:
        total += leds[int(i)]
        
    print(f'{total} leds')
