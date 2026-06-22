import pandas as pd
from pathlib import Path

ARCHIVO = "resultados.xlsx"


def guardar_o_actualizar_resultado(nombre, puntaje, modo, categoria):

    # Si el archivo existe, lo cargamos
    if Path(ARCHIVO).exists():
        df = pd.read_excel(ARCHIVO)
    else:
        df = pd.DataFrame(columns=["Usuario", "Puntaje", "Dificultad", "Categoria"])

    # Si el usuario ya existe
    if nombre in df["Usuario"].values:

        indice = df[df["Usuario"] == nombre].index[0]

        # Solo actualiza si el nuevo puntaje es mayor
        if puntaje > df.at[indice, "Puntaje"]:
            df.at[indice, "Puntaje"] = puntaje
            df.at[indice, "Dificultad"] = modo
            df.at[indice, "Categoria"] = categoria

    else:
        # Crear nueva fila
        nueva_fila = pd.DataFrame(
            [[nombre, puntaje, modo, categoria]],
            columns=["Usuario", "Puntaje", "Dificultad", "Categoria"]
        )

        df = pd.concat([df, nueva_fila], ignore_index=True)

    # Ordenar ranking por puntaje
    df = df.sort_values(by="Puntaje", ascending=False)

    # Guardar en Excel
    df.to_excel(ARCHIVO, index=False)

    return df