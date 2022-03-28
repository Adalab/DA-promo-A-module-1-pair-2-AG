import random

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}


# Inicio del juego
print("Bienvenidos al oraculo")

# Elegir una categoria
print("Elige una categoria de las siguientes, usando el numero")
categorias = int(input('1:Colors,' '2:Shapes,' '3:Fruits,' '4:Animals '))
print("Has elegido la categoria", categorias)

# El ordenador calcula la categoria a partir del input numerico del usuario
lista_claves = list(words.keys())
nombre_categoria = lista_claves[categorias - 1]

# El ordenador elige una palabra de la categoria
word_list = words[nombre_categoria]
word_secreta = random.randint(0, len(word_list)-1)

# Adivinar una palabra
print("Adivina la palabra de la categoria elegida, escribela")
palabra_elegida = input()
print("Has elegido: ", palabra_elegida)

# Era la palabra aleatoria?
print("¿Era la palabra que buscabamos?")
print(bool(palabra_elegida == (word_list[word_secreta])))

# Fin del juego
print("Esta era la palabra secreta", (word_list[word_secreta]))