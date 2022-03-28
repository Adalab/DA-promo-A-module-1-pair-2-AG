from pickle import FALSE
import random

# Variables
palabras = "mochila freidora lampara peluche botella jabon".split()
intentos_permitidos = 12
intentos = 1
errores = []

# Strings
# Inicio
print("Bienvenidos al oraculo")
print("Hoy jugaremos al ahorcado")
print("Tienes", intentos_permitidos, "para adivinar la palabra. ¿Seras capaz?")

# Variables calculadas
palabra_secreta = palabras[random.randint(0, len(palabras)-1)].upper()
tablero = ["_"]*len(palabra_secreta)

print("Intento 1:")

print(tablero)
letraUsuaria = input()

#convierto la palabra secreta en una lista para separar cada letra que la compone con un indice cada una
#para que en el bucle se pueda ir recorriendo
aciertos = list(palabra_secreta)

#while lo utilizo para que mientras los intentos no lleguen a los maximos permitios siga recorriendo la lista
#termino ese while con un if cuando llegue la usuaria a los intentos permitios, ya habra perdido

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