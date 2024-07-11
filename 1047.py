hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

duracao_horas = hora_final - hora_inicial
duracao_minutos = minuto_final - minuto_inicial

if duracao_minutos < 0:
    duracao_minutos += 60
    duracao_horas -= 1

if duracao_horas < 0:
    duracao_horas += 24

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")