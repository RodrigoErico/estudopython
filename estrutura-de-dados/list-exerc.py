notas = [2, 4.5, 5, 9, 10]

i = 0
total = 0

# verifica o tamanho da lista
qtd = len(notas)

# para percorrer a lista
while i < qtd:
    total += notas[i]
    i += 1

print("O total das notas é :", total)

media = total / qtd
print("A media das notas é:", media)