
# Inicio del juego y explicacion a la usuaria
print("Comencemos el juego del tres en raya")
print("Para jugar debes elegir entre 'x' o 'o' y dos coordenadas entre 1 y 3")

#Definir el tablero con todo "-"
tablero = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]


# Imprimir tablero
print(tablero[0][0] + " | " + tablero[0][1] + " | " + tablero[0][2])
print(tablero[1][0] + " | " + tablero[1][1] + " | " + tablero[1][2])
print(tablero[2][0] + " | " + tablero[2][1] + " | " + tablero[2][2])

# Input de la usuaria
coor_usuaria= input().split(" ")
valor1 = coor_usuaria[0]
coordenadas = coor_usuaria[1].split(",")
#coor = tuple(int((num)-1 for num in coor.split(","))) #Otra forma de hacerlo

# Actualizar tablero (siguiente paso)
tablero[int(coordenadas[0])-1][int(coordenadas[1])-1] = valor1

print(tablero[0][0] + " | " + tablero[0][1] + " | " + tablero[0][2])
print(tablero[1][0] + " | " + tablero[1][1] + " | " + tablero[1][2])
print(tablero[2][0] + " | " + tablero[2][1] + " | " + tablero[2][2])
#coor = tuple(int(co)-1 for co in coor.split(","))

# Input de la usuaria 2
coor = input().split(" ")
valor2 = coor[0]
coordenadas = coor[1].split(",")

# Actualizar tablero con el input de la usuaria 2
tablero[int(coordenadas[0])-1][int(coordenadas[1])-1] = valor2

print(tablero[0][0] + " | " + tablero[0][1] + " | " + tablero[0][2])
print(tablero[1][0] + " | " + tablero[1][1] + " | " + tablero[1][2])
print(tablero[2][0] + " | " + tablero[2][1] + " | " + tablero[2][2])


# Convertir los caracteres del board a una sola lista
#board_list = sum(tablero,[])

# Sacar los elementos únicos que no sean "-"
print("Las usuarias han utilizado {",valor1,",",valor2,"}")

# Final del juego
print("Gracias por participar")