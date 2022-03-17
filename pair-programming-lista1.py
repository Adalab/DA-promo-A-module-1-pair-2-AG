import random

x = "Bienvenidos al oraculo"
print(x)

str_input = "Escribe una lista de cinco numeros: " 

num_list = list(int(num) for num in input(str_input).strip().split())

lim_inferior = min(num_list)
lim_superior = max(num_list)

print("El numero esta entre", lim_inferior, "y", lim_superior)
numero_secreto = random.randint(lim_inferior,lim_superior)


print("Y el numero es...", numero_secreto, "¡Espero que hayas acertado!")

bool_borde_lista = numero_secreto in num_list
print(bool_borde_lista)



