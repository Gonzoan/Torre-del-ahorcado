import random
class Ahorcado:

    def __init__(self):
        #esto define los valores iniciales, preparándose para iniciar la categoría que próximamente será puesta en random
        #junto a la palabra también random(ya puesta pero no probada)
        self.categoria = ""
        self.nivel = 1
        self.palabra = ""
        self.vida = 6
    def cargar_palabras(self, categoria, nivel, idioma):
    
        self.categoria = categoria  
        self.nivel = nivel
    
        ruta = f"palabras/{categoria}/{idioma}/nivel{nivel}.txt"
    
        with open(ruta, "r", encoding="utf-8") as archivo:
            palabras = archivo.read().splitlines()
        
        self.palabra = random.choice(palabras)
        
    