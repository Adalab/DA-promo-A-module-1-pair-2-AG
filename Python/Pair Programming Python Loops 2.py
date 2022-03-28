from pickle import FALSE
import random

# Variables
palabras = "mochila freidora lampara peluche botella jabon anacardo bootcamp sabana".split()
intentos_permitidos = 12
intentos = 1
errores = []

# Inicio
print("Bienvenidos al oraculo")
print("Hoy jugaremos al ahorcado")
print("Tienes", intentos_permitidos, "intentos para adivinar la palabra. ¿Seras capaz?")

# Variables calculadas
palabra_secreta = palabras[random.randint(0, len(palabras)-1)].upper() 
tablero = ["_"]*len(palabra_secreta)

#Input de la usuaria
print("Introduce la letra en mayuscula")
print("Intento 1:")

print(tablero)
letraUsuaria = input()

#palabra secreta convertida en lista
aciertos = list(palabra_secreta)

#while y for lo utilizamos para repetir el bucle
while intentos < intentos_permitidos:
    bool_error = True
    for indice in range(0, len(aciertos)):
        if letraUsuaria == aciertos[indice]:
            tablero[indice] = letraUsuaria  # Actualizar la palabra 
            bool_error = False
    if bool_error == True:  
        errores.append(letraUsuaria)   # Actualizar los fallos
    print(tablero,errores)  # Comunicar el estado del juego a la usuaria
    if tablero == aciertos:
        print("Has acertado, enhorabuena")
        break # Parar el juego si la palabra ha sido adivinada
    intentos = intentos + 1
    print("Intento", intentos, ":")
    letraUsuaria = input()

# Final del juego 
if intentos == intentos_permitidos:
    print(tablero,errores)
    print("Has acabado con todos los intentos, intentalo de nuevo") 

print("La palabra secreta era...", palabra_secreta)