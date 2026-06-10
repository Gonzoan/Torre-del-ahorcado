from pathlib import Path
class SelectorTema:

    def __init__(self):

        # Lista donde se guardarán las categorías
        self.Tematicas = []

    # Función para mostrar las categorías
    def SeleccionTematicas(self):

        # Buscar todas las carpetas dentro de "palabras"
        self.Tematicas = [
            carpeta.name #es una funcion de Path para extraer el nombre de un archivo o carpeta
            for carpeta in Path("palabras").iterdir() #Path abre la carpeta palabras e iterdir recorre lo que se encuentra adentro
            if carpeta.is_dir() #is.dir revisa si el archivo que selecciono es carpeta o no
        ]

        # Mostrar título
        print("\n----- SELECCIONA UNA CATEGORÍA -----\n")

        contador = 1

        for categoria in self.Tematicas: #se crea la variable categoria

            print(f"{contador}. {categoria}") #el for avanza automaticamente la categoria no hace falta aclarar que valor de la lista

            contador += 1

        opcion = int(input("\nSeleccione una opción: "))

        # Obtener el nombre de la categoría
        categoria_seleccionada = self.Tematicas[opcion - 1]

        return categoria_seleccionada

class SelectorIdioma:

    # Función para seleccionar el idioma
    def SeleccionIdioma(self,categoria):
        # Buscar todas las carpetas dentro de "palabras"
        self.Idioma = [
            carpeta.name  # es una funcion de Path para extraer el nombre de un archivo o carpeta
            for carpeta in Path(f"palabras/{categoria}/").iterdir() #se abre desde la carpeta de la categoria anteriormente seleccionada
            # Path abre la carpeta palabras e iterdir recorre lo que se encuentra adentro
            if carpeta.is_dir()  # is.dir revisa si el archivo que selecciono es carpeta o no
        ]

        contador2 = 1

        for categoria in self.Idioma: #se crea la variable categoria

            print(f"{contador2}. {categoria}") #el for avanza automaticamente la categoria no hace falta aclarar que valor de la lista

            contador2 += 1

        opcion = int(input("\nSeleccione una opción: "))

        IdiomaSeleccionado = self.Idioma[opcion - 1]

        return IdiomaSeleccionado




"""

if __name__ == "__main__":

    categoria = "musica"

    selector = SelectorIdioma()

    categoria = selector.SeleccionIdioma(categoria)

"""