entrada_dia_inicio = input()
dia_inicio = int(entrada_dia_inicio.split("Dia ")[1])

hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))

entrada_dia_fim = input()
dia_fim = int(entrada_dia_fim.split("Dia ")[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

total_segundos_inicio = (dia_inicio * 24 * 60 * 60) + (hora_inicio * 60 * 60) + (minuto_inicio * 60) + segundo_inicio
total_segundos_fim = (dia_fim * 24 * 60 * 60) + (hora_fim * 60 * 60) + (minuto_fim * 60) + segundo_fim
diferenca_segundos = total_segundos_fim - total_segundos_inicio

dias = diferenca_segundos // (24 * 60 * 60)
diferenca_segundos %= (24 * 60 * 60)
horas = diferenca_segundos // (60 * 60)
diferenca_segundos %= (60 * 60)
minutos = diferenca_segundos // 60
segundos = diferenca_segundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
