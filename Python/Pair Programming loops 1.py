import math
import random

# Variables numéricas
lim_superior = 10
lim_inferior = 1


# Cantidades calculadas
intentos_permitidos = round(math.log(lim_superior - lim_inferior + 1.2))
numero_secreto = random.randint(lim_inferior,lim_superior)
intentos_maximos = 3
intentos = 1

# Inicio del juego
print("Bienvenidos al oraculo")

print("Adivina el numero del ", lim_inferior, "al ", lim_superior)

# Adivinar con mas de un intento
print("Tienes 3 intentos para adivinar el numero ¿Seras capaz?")

print("Intento 1: ")
intentoUsuaria = input()

#Bucle hasta llegar a los intentos maximos 
while intentos < intentos_maximos:
    if int(intentoUsuaria) == numero_secreto:
        print("¡Enhorabuena has acertado!")
        break
    else:
        print("Has fallado, vuelve a intentarlo")
        if int(intentoUsuaria) < numero_secreto:
            print("El numero que has elegido es mas bajo que el numero secreto")
        else:
            print("El numero que has elegido es mas alto que el numero secreto")
        intentos = intentos + 1
        print("Intento", intentos, ":")
        intentoUsuaria = int(input())
        if intentos == intentos_maximos:
            if int(intentoUsuaria) == numero_secreto:
                print("¡Enhorabuena has acertado!")
                break     
        
    
# Fin del juego
print("El numero secreto era....", numero_secreto,)