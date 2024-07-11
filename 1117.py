lista = []

while len(lista) < 2:
    nota = float(input())

    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        lista.append(nota)

media = sum(lista) / len(lista)
print(f"media = {media:.2f}")