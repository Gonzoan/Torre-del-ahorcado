import pandas as pd
from pathlib import Path

ARCHIVO = "resultados.xlsx"


def guardar_o_actualizar_resultado(nombre, puntaje):

    # Si el archivo ya existe, lo cargamos
    if Path(ARCHIVO).exists():
        df = pd.read_excel(ARCHIVO)
    else:
        df = pd.DataFrame(columns=["Usuario", "Puntaje"])

    # Si el usuario ya existe, actualiza su puntaje (si es mayor)
    if nombre in df["Usuario"].values:

        indice = df[df["Usuario"] == nombre].index[0]

        # Solo actualiza si el nuevo puntaje es mayor
        if puntaje > df.at[indice, "Puntaje"]:
            df.at[indice, "Puntaje"] = puntaje

    else:
        # Agrega nuevo usuario
        nueva_fila = pd.DataFrame([[nombre, puntaje]], columns=["Usuario", "Puntaje"])
        df = pd.concat([df, nueva_fila], ignore_index=True)

    # Ordenar de mayor a menor puntaje
    df = df.sort_values(by="Puntaje", ascending=False)

    # Guardar en Excel
    df.to_excel(ARCHIVO, index=False)

    return df