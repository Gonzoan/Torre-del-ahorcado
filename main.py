from juego import Ahorcado
from MenuSeleccionTema import SelectorTema, SelectorIdioma
from puntuacion import calcular_puntaje_total
from resultados import guardar_o_actualizar_resultado

print("""
======================================
|  BIENVENIDO AL JUEGO DEL AHORCADO  |
======================================
""")

nombre_jugador = input("Escriba su nombre para empezar: ")
print(f"\n¡Bienvenido, {nombre_jugador}!\n")

selector = SelectorTema()
categoria = selector.SeleccionTematicas()

selector_idioma = SelectorIdioma()
Idioma = selector_idioma.SeleccionIdioma(categoria)

juego = Ahorcado()
#juego.cargar_palabras(categoria, 1,Idioma) #llama la logica de selección de las palabras
#print(juego.palabra) #prueba de que si sirva la función y la muestre en consola

#En caso de completar todo el juego
victoria_total = True

puntajes_niveles = []

#Los niveles del 1 al 5
for nivel_actual in range (1,6):
    print("\n" + "="*35)
    print(f"    CARGANDO: NIVEL {nivel_actual} DE 5")
    print("="*35)

    #Cargamos la nueva palabra del nuevo nivel
    juego.cargar_palabras(categoria, nivel_actual, Idioma)

    #Iniciamos la logica del juego del nuevo nivel y palabra
    juego.jugar()

    if juego.vida > 0:

        vidas_perdidas = 9 - juego.vida

        puntos_nivel = max(0, 20 - (vidas_perdidas * 2))

        puntajes_niveles.append(puntos_nivel)

        print(f"Puntos obtenidos en este nivel: {puntos_nivel}")

    if juego.vida == 0:
        #Si se quedo sin vidas, ya se acaba todo el juego
        print(f"{nombre_jugador} llegó hasta el nivel {nivel_actual}.")
        victoria_total = False
        break

    if nivel_actual < 5:
        print("Cargando el siguiente nivel...")
        input("Presiona Enter para continuar")

#Calcula el puntaje total utilizando una función recursiva
puntaje_total = calcular_puntaje_total(puntajes_niveles)

print("\n" + "="*35)
print(f"PUNTAJE FINAL: {puntaje_total}")
print("="*35)

# Guardar o actualizar en Excel
tabla = guardar_o_actualizar_resultado(nombre_jugador, puntaje_total)

print("\n" + "="*40)
print("TABLA DE PUNTAJES")
print("="*40)

print(tabla.to_string(index=False))

if victoria_total:
    print("=======================================================")
    print(f"¡Felicitaciones {nombre_jugador}! Completaste todos los niveles.!!")
    print(f"Puntaje total obtenido: {puntaje_total}")
    print("=======================================================")