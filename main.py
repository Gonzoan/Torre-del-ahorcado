from juego import Ahorcado
from MenuSeleccionTema import SelectorTema, SelectorIdioma

seleccion = 0

if seleccion == 0:

    print("I---- bienvenido a la torre del ahorcado ----I")
    print(" ")
    seleccion = int(input("            escriba 1 para empezar: "))
    print(" ")

if seleccion == 1:

    selector = SelectorTema()
    categoria = selector.SeleccionTematicas()

    SelectorIdioma = SelectorIdioma()
    Idioma = SelectorIdioma.SeleccionIdioma(categoria)

    juego = Ahorcado()
    juego.cargar_palabras(categoria, 1,Idioma)
    print(juego.palabra) #prueba de que si sirva la función y la muestre en consola



