import random

#Inicio 
print("Bienvenidos al oraculo")

#Cadenas fijas de texto
str_input = "Escribe una lista de seis numeros: " 

#Propiedades de la lista
num_list = list(int(num) for num in input(str_input).strip().split())

lim_inferior = min(num_list)
lim_superior = max(num_list)

#Cantidades calculadas
print("El numero esta entre", lim_inferior, "y", lim_superior)
numero_secreto = random.randint(lim_inferior,lim_superior)

#¿Se ha adivinado el numero?
print("¿Has adivinado el numero?")
bool_borde_lista = numero_secreto in num_list
print(bool_borde_lista)

#Fin del juego
print("Y el numero es...", numero_secreto, "¡Espero que hayas acertado!")

