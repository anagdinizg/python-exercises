while True:
    notas = []

    while len(notas) < 2:
        nota = float(input())

        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            notas.append(nota)

    media = sum(notas) / 2
    print(f"media = {media:.2f}")

    while True:
        print('novo calculo (1-sim 2-nao)')
        opcao = int(input())

        if opcao == 1 or opcao == 2:
            break
        else:
            continue

    if opcao == 2:
        break
