def calcula_media(notas):
    media = sum(notas) / len(notas)

    if len(notas) % 2 == 0:
        # numero par de elementos
        indice_ponto_central_menor = int(len(notas)/2 - 1)
        indice_ponto_central_maior = int(len(notas)/2)
        ponto_central_menor = notas[indice_ponto_central_menor]
        ponto_central_maior = notas[indice_ponto_central_maior]

        mediana = (ponto_central_menor + ponto_central_maior)/2
    else:
        # numero impar de elementos
        notas_ordenadas = sorted(notas)
        indice_mediana = int(len(notas)/2)
        mediana = notas_ordenadas[indice_mediana]

    return media, mediana


resultado_media, resultado_media_impar = calcula_media([5, 6, 8, 5])
print(resultado_media)
print(resultado_media_impar)
