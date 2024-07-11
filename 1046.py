hora_inicial, hora_final = map(int, input().split())

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = 24 - hora_inicial + hora_final

if duracao < 1:
    duracao = 24 + duracao

print("O JOGO DUROU", duracao, "HORA(S)")