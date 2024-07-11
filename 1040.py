entrada = input()

N1, N2, N3, N4 = map(float, entrada.split())

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

if media >= 7.0:
    print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")
elif media < 5.0:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")
else:
    print("Media: {:.1f}".format(media))
    print("Aluno em exame.")
    exame = float(input())
    media_final = (media + exame) / 2
    print("Nota do exame:", exame)
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))