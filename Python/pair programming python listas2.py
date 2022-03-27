import random

# Variables numéricas

lim_inferior = 0
lim_superior = 20
longitud_lista = 10



# Cadenas fijas de texto
print("Esta lista aleatoria contiene", longitud_lista, "numeros entre el", lim_inferior, "y", lim_superior)

# User input
print("¿Cual crees que es?")
numero_usuario = input()


# Cantidades calculadas
num_list = random.sample(range(lim_inferior, lim_superior), longitud_lista)
index = num_list.index(int(numero_usuario))

# Han adivinado un elemento?
print("¿Has adivinado el numero?")
bool_numero = int(numero_usuario) in num_list
print(bool_numero)

# Si adivinaron uno, dónde estaba?
if num_list.count(numero_usuario): index = num_list.index(numero_usuario)
if index >= 0: print("Estaba en el sitio", str(index+1) + ", índice", str(index)+".")

print("Esta era la lista de numeros:", num_list)


# Fin del juego