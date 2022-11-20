# iteraveis  dict, set, list, tuple

notas = {12, 2, 34}

"""
nao funciona em set
i = 0
while i < len(notas):
    n = notas[i]
"""
for i in notas:
    print(i)

# dict.keys
# dict.values
# dict.items

user = {
    "name": "Rodrigo",
    "admin": True,
}

for a in user.items():
    print(a)

# or

for k, v in user.items():
    print(k, v)