# Dada uma lista de números inteiros, escreva um programa que calcula a soma de
# todos os números na lista.
import statistics

lista1 = [1, 10, 20, 35, 22, 12]

i = 0
total = 0

while i < len(lista1):
    total += lista1[i]
    i += 1

print(total)

# Data uma lista de números inteiros, escreva um programa que calcula a média dos
# números na lista. O resultado não deve incluir números decimais.

lista2 = [1, 10, 20, 35, 22, 12]

mean = statistics.mean(lista2)
print(int(mean))
# or
media = sum(lista2) // len(lista2)
print(media)

# Escreva uma programa que calcula a média das notas de todos os alunos.

alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

print(alunos[1])