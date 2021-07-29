# https://www.urionlinejudge.com.br/judge/en/problems/view/2752

val = 'AMO FAZER EXERCICIO NO URI'
formatado = ['%s', '%30s', '%.20s', '%-20s', '%-30s',
            '%.30s', '%30.20s', '%-30.20s']
for pos in formatado:
    print(f'<{pos}>' % val)
