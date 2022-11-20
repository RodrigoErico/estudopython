notas = [8, 9, 23, 4]

# adicionar arquivo na ultima posicao
notas.append(100)
print(notas[4])

# ordenar lista
notas.sort()

# ordenar lista invertendo
notas.sort(reverse=True)
print(notas)

# remove o ultimo elemento
notas.pop()

# adicionar na posiçao especifica
notas.insert(0, 90)
print("apos a inserção")
print(notas)

# remover na posicao especifica
notas.pop(0)
print(notas)