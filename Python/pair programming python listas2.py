import random

# Variables numéricas
index = -1
lim_inferior = 1
lim_superior = 20
longitud_lista = 10


# Cadenas fijas de texto
print("Esta lista aleatoria contiene", longitud_lista, "numeros entre el", lim_inferior, "y", lim_superior)

# User input
print("¿Cual crees que es?")
numero_usuario = int(input())


# Cantidades calculadas
num_list = random.sample(range(lim_inferior, lim_superior), longitud_lista)


# ¿Han adivinado un elemento?
print("¿Has adivinado el numero?")
bool_numero = bool(int(numero_usuario) in num_list)
print(bool_numero)


# Si adivinaron, y donde estaba
if num_list.count(numero_usuario): 
    index = num_list.index(numero_usuario)

if index >= 0: 
    print("Estaba en el sitio", str(index+1) + ", índice", str(index)+".")


# Fin del juego
print("Esta era la lista de numeros:", num_list)
