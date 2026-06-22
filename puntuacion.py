def calcular_puntaje_total(lista_puntajes, indice=0):

    # Caso base: ya recorrimos toda la lista
    if indice >= len(lista_puntajes):
        return 0

    # Caso recursivo:
    return lista_puntajes[indice] + calcular_puntaje_total(lista_puntajes, indice + 1)

