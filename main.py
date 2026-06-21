from juego import Ahorcado
from MenuSeleccionTema import SelectorTema, SelectorIdioma

seleccion = 0

if seleccion == 0:

    print("""
======================================
|  BIENVENIDO AL JUEGO DEL AHORCADO  |
======================================
""")
    print(" ")
    seleccion = int(input("     Escriba 1 para empezar: "))
    print(" ")

if seleccion == 1:

    selector = SelectorTema()
    categoria = selector.SeleccionTematicas() #funcion para selecciónar las tematicas, viene de MenuSeleccionTema.py

    SelectorIdioma = SelectorIdioma()
    Idioma = SelectorIdioma.SeleccionIdioma(categoria) #funcion para seleccionar el idioma, tambien viene de MenuSeleccionTema.py

    juego = Ahorcado()
    juego.cargar_palabras(categoria, 1,Idioma) #llama la logica de selección de las palabras
    #print(juego.palabra) #prueba de que si sirva la función y la muestre en consola
    #En caso de completar todo el juego
    victoria_total = True

    #Los niveles del 1 al 5
    for nivel_actual in range (1,6):
        print("\n" + "="*35)
        print(f"    CARGANDO: NIVEL {nivel_actual} DE 5")
        print("="*35)
        #Cargamos la nueva palabra del nuevo nivel
        juego.cargar_palabras(categoria, nivel_actual, Idioma)
        #Iniciamos la logica del juego del nuevo nivel y palabra
        juego.jugar()
        
        if juego.vida == 0:
            #Si se quedo sin vidas, ya se acaba todo el juego
            print(f"Fin del juego. Te quedaste en el nivel {nivel_actual}")
            break

        if nivel_actual < 5:
            print("Cargando el siguiente nivel...")
            input("Presiona Enter para continuar")

    if victoria_total:
        print("Pasaste todos los niveles del ahorcado")