# Unindo conjuntos

number_1 = {99, 34, 45, 99}
number_2 = set([90, 78, 99, 100])

# pode se usar o pipe | para unir
print("Unidos:", number_1.union(number_2))

is_equal = number_1.union(number_2) == number_1 | number_2
print("São iguais:", is_equal)

# verifica qual elemento que se repeti
print("Numero que se repeti:", number_1.intersection(number_2))

# pode se usar o & comercial para verificar se existe identicos
is_equal_2 = number_1.intersection(number_2) == number_1 & number_2
print("São iguais:", is_equal_2)

# elementos que nao se repetem
print("Numeros que nao se repetem:", number_1.difference(number_2))

# usar o operador de - para verificar o que são diferentes
is_qual_3 = number_1.difference(number_2) == number_1 - number_2
print("Verificou se é diferente:", is_qual_3)
