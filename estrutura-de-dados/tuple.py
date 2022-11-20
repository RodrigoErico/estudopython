x = (5, 34)

print(x[0])
print(type(x))

# person = ("Nome", 23, True)

# ValueError: não há valores suficientes para desempacotar (esperado 3, obteve 1)
person = [
    ("Nome", 23, True)
]
name, age, admin = person
print(name, age, admin)


team = (
    ("Turma 23", 3),
    [2, 3, 4]
)

print(type(team))

# tuplas nao pode ser alterada ou acresentar itens

