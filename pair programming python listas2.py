import random

# Variables numéricas
index = -1
lim_inferior = 0
lim_superior = 20
longitud_lista = 10


# Cadenas fijas de texto
print("Esta lista aleatoria contiene", longitud_lista, "numeros entre el", lim_inferior, "y", lim_superior)

# User input
input("¿Cual crees que es?: ")
a = input()


# Cantidades calculadas
num_list = random.sample(range(lim_inferior, lim_superior), longitud_lista)

# Inicio del juego

# Propiedades de la lista aleatoria

# Han adivinado un elemento?

# Si adivinaron uno, dónde estaba?
if num_list.count(str_input): index = num_list.index(str_input)
if index >= 0: print("Estaba en el sitio", str(index+1) + ", índice", str(index)+".")

# Fin del juego