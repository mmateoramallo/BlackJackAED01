"""
Para el presente Trabajo Práctico se pide simular una única mano con un jugador contra el crupier.
Se debe determinar el ganador de la mano considerando quien haya alcanzado un puntaje más cercano a 21 sin pasarse.
A cada jugador se le pueden dar hasta 3 cartas, la tercera carta sólo dependerá del puntaje alcanzado con las dos anteriores y no es opcional para el usuario.
El AS vale 11 mientras no se pase de 21 y 1 en caso contrario tanto para el croupier como para el jugador. Como es una sola jugada podemos considerar posible que se obtenga la misma carta en la jugada (tanto el mismo jugador, como el croupier).
No se considera el Blackjack o 21 natural
No hay apuestas en juego.

c. Requerimiento: Se pide desarrollar un programa en Python que cumpla las siguientes consignas:

Simular la partida generando en forma aleatoria los valores de las cartas obtenidas por ambos participantes(número o figura y palo), mostrando en cada caso la carta y el puntaje parcial que obtiene con la misma.
Determinar quién ha obtenido el mayor puntaje, el jugador o el croupier. Considerar que pueden empatar.
Determinar si el palo de la primera carta del jugador es el mismo que el obtenido por el croupier en su primera carta.
Si además de coincidir en el palo es el mismo número (tomando en consideración que las cartas se pueden repetir) o figura mostrar un mensaje adicional.
"""

#Importando el modulo random
import random

print('*'*25, 'BlackJack', '*'*25)

#Asignacion nombres, para declarar el ganador

player = input('Ingrese su nombre: ')
croupier = 'Croupier'

#Declaracion de variables

cartas = (1,2)

palos = ('Picas', 'Trebol', 'Corazones', 'Diamantes')

#Generar Aleatoriamente los palos y valores

print('*'*25, 'Generando Tirada', '*'*25)

valor_carta_jugador = random.choice(cartas)

#Validar en caso de que sea un AS la primera carta
if valor_carta_jugador == 1:
    valor_carta_jugador = 11
else:
    valor_carta_jugador = random.choice(cartas)

valor_palo_jugador = random.choice(palos)

#Carta Croupier

valor_carta_croupier = random.choice(cartas)

#Validar en caso de que sea un AS la primera carta
if valor_carta_croupier == 1:
    valor_carta_croupier = 11
else:
    valor_carta_croupier = random.choice(cartas)

valor_palo_croupier = random.choice(palos)

#Visualizacion de valores

print('La primera carta del jugador es: ', str(valor_carta_jugador))
print('La primera carta del croupier es: ', str(valor_carta_croupier))


###
#Generar Segunda Tirada
###

print('*'*25, 'Generando Segunda Tirada', '*'*25)

valor_segunda_carta_jugador = random.choice(cartas)

#Validacion AS

if valor_segunda_carta_jugador == 1:
    valor_segunda_carta_jugador = 11
else:
    valor_segunda_carta_jugador = random.choice(cartas)

valor_segundo_palo_jugador = random.choice(palos)

#Segunda Carta Croupier

valor_segunda_carta_croupier = random.choice(cartas)

#Validacion AS

if valor_segunda_carta_croupier == 1:
    valor_segunda_carta_croupier = 11
else:
    valor_segunda_carta_croupier = random.choice(cartas)

valor_segundo_palo_croupier = random.choice(palos)

#Visualizacion de valores

print('La segunda carta del jugador es: ', str(valor_segunda_carta_jugador))
print('La segunda carta del croupier es: ', str(valor_segunda_carta_croupier))

#Puntaje Total

puntaje_jugador = valor_carta_jugador + valor_segunda_carta_jugador

puntaje_croupier = valor_carta_croupier + valor_segunda_carta_croupier

print('Puntaje Total Jugador:',puntaje_jugador)
print('Puntaje Total Croupier:',puntaje_croupier)





