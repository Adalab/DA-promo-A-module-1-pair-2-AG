# Variables predefinidas
bienvenida = "Comencemos el juego del tres en raya"

#Definir el tablero con todo "-"
tablero = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

# Inicio del juego
print(bienvenida)

# Imprimir tablero
print(tablero[0][0] + " | " + tablero[0][1] + " | " + tablero[0][2])
print(tablero[0][0] + " | " + tablero[0][1] + " | " + tablero[0][2])
print(tablero[0][0] + " | " + tablero[0][1] + " | " + tablero[0][2])
# Input de la usuaria

jugador1 = input()
coor = jugador1
coor = tuple(int((num)-1 for num in coor.split(",")))

# Actualizar tablero

# Imprimir tablero

# Input del usuario

#coor = tuple(int(co)-1 for co in coor.split(","))

# Actualizar tablero

# Imprimir tablero

# Convertir los caracteres del board a una sola lista
#board_list = sum(tablero,[])

# Sacar los elementos únicos que no sean "-"

# Final del juego