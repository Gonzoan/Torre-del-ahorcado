import random
from Munecoahorcado import Animacion_muneco
class Ahorcado:

    def __init__(self):
        #esto define los valores iniciales, preparándose para iniciar la categoría que próximamente será puesta en random
        #junto a la palabra también random(ya puesta pero no probada)
        self.categoria = ""
        self.nivel = 1
        self.palabra = ""
        self.vida = 9
        self.letras_adivinadas = []
        self.letras_intentadas = []
        self.modo = "normal"

    def cargar_palabras(self, categoria, nivel, idioma):
    
        self.categoria = categoria  
        self.nivel = nivel
    
        ruta = f"palabras/{categoria}/{idioma}/nivel{nivel}.txt"
    
        with open(ruta, "r", encoding="utf-8") as archivo:
            palabras = archivo.read().splitlines()
        #Pasa las palabras a mayusculas
        self.palabra = random.choice(palabras).upper()
        #Resetea todas las listas para el siguiente nivel
        self.letras_adivinadas = []
        self.letras_intentadas = []

        if self.modo == "normal":
            self.vida = 9

        #Algunas palabras tienen espacios, se agregan de una vez
        if " " in self.palabra:
            self.letras_adivinadas.append(" ")
    
    def Mostrar_palabra(self):
        #Esta funcion mostrar por pantalla la palabra oculta en ______
        palabra_oculta = ""
        #Recoremos la palabra letra por letra 

        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                #Si el jugador adivina la letra esta se imprime en pantalla
                palabra_oculta += letra + " "
            elif letra == " ":
                #Si tiene un espacio que se muestre en pantalla
                palabra_oculta += "   "
            else:
                #Si no hay ninguna adivinada todas son "___"
                palabra_oculta += "_ "
        
        #Retornar la palabra sin espacio en blanco final
        return palabra_oculta.strip()
    
    def jugar(self):
        print("\tInicia el juego!")
        #ciclo de juego donde el jugador adivina la palabra
        while self.vida > 0 and "_" in self.Mostrar_palabra():
            print("")
            print(Animacion_muneco(9 - self.vida))
            print(f"Palabra: {self.Mostrar_palabra()}")#La palabra actual
            print(f"Vidas restantes: {self.vida}") # Las vidas restantes
            print (f"Letras intentadas: {','.join(self.letras_intentadas)}")# Muestra las letras intentadas
            #Menu donde se muestra las estadisticas actuales del juego


            #Pide la letra y la convierte en mayuscula
            letra_jugador = input("\nIntroduce una letra: ").upper()

            #Comprueba que la letra sea solo una y no acepta frases largas
            if len(letra_jugador) != 1 or not letra_jugador.isalpha():
                print("Letra no valida, por favor vuelva a introducir la letra")
                print("="*35)
                continue

            #Si se ingresa una letra ya introducidad anterior mente se le da otra oportunidad
            if letra_jugador in self.letras_intentadas:
                print(f"Ya intentaste esta letra antes")
                print("="*35)
                continue

            #Se agrega la letra nueva a la lista
            self.letras_intentadas.append(letra_jugador)

            #Comprueba que la letra este en la palabra aleatoria
            if letra_jugador in self.palabra:
                print("Acertaste!!")
                self.letras_adivinadas.append(letra_jugador)
            else:
                #Si falla la animacion cambia
                print("Fallaste!!")
                self.vida -= 1
            print("="*35)
        #Si no pierde todas las vidas pada al siguiete nivel
        if self.vida > 0:
            print(Animacion_muneco(9 - self.vida))
            print(f"Nivel {self.nivel} completado!!\nLa palabra era: {self.palabra}")
        else:
            #Pierde totalmente
            print(Animacion_muneco(9))
            print(f"Has sido ahorcado en el nivel {self.nivel}.\nLa palabra era: {self.palabra}")
            print("======================")
            print("     GAME OVER!!")
            print("======================")