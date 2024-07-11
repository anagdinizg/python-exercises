alcool = 0
gasolina = 0
diesel = 0

while True:
    tipo_combustivel = int(input())

    if tipo_combustivel == 1:
        alcool += 1
    elif tipo_combustivel == 2:
        gasolina += 1
    elif tipo_combustivel == 3:
        diesel += 1
    elif tipo_combustivel == 4:
        break
    else:
        continue

print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)