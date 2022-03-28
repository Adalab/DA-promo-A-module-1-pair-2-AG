import math
import random

# Variables numéricas
lim_superior = 6
lim_inferior = 1


# Cantidades calculadas
intentos_permitidos = round(math.log(lim_superior - lim_inferior + 1.2))
numero_secreto = random.randint(lim_inferior,lim_superior)

# Inicio del juego
print("Bienvenidos al oraculo")
print("A ver si puedes adivinar el numero del 1 al 6")

# Adivinar 1 intento
print("Intento 1:" + input())

# Fin del juego
print("Y el numero es...", numero_secreto, "¡Espero que hayas acertado!")
