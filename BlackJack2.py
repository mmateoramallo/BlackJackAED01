#Importando el modulo random
import random

print('*'*25, 'BlackJack', '*'*25)

#Asignacion nombres, para declarar el ganador

player = input('Ingrese su nombre: ')

#Validar de que la persona haya ingresado su nombre

if player == "":
    player = input('Ingrese su nombre !CORRECTAMENTE : ')

#Variables

#figuras = ('J', 'Q', 'K', 'AS')

cartas = (2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'AS')

palos = ('Picas', 'Trebol', 'Corazones', 'Diamantes')


#Generar Aleatoriamente los palos y valores

print('*'*25, 'Generando Primera Tirada', '*'*25)

carta_jugador = random.choice(cartas)

if carta_jugador == 'J' or carta_jugador == 'K' or carta_jugador == 'Q':
    carta_jugador = 10
elif carta_jugador == 'AS':
    carta_jugador = 11

palo_primera_carta_jugador = random.choice(palos)

print('La carta de', player, 'es el numero', carta_jugador, 'cuyo palo es', palo_primera_carta_jugador)

#Primera Carta Croupier

carta_croupier = random.choice(cartas)

if carta_croupier == 'J' or carta_croupier == 'K' or carta_croupier == 'Q':
    carta_croupier = 10
elif carta_croupier == 'AS':
    carta_croupier = 11

palo_primera_carta_croupier = random.choice(palos)

print('Carta Croupier: ', carta_croupier, 'palo' , palo_primera_carta_croupier)

#Puntaje De Ambos Jugadores

puntuacion_player = carta_jugador

print('-'*25,'El puntaje total de', player, 'es de:', puntuacion_player, 'puntos','-'*25)

puntuacion_croupier = carta_croupier

print('-'*25,'El puntaje total del croupieres de:', puntuacion_croupier, 'puntos','-'*25)


#----------------------------------------------------#
#Segunda Mano De Cartas

print('*'*25, 'Generando Segunda Tirada', '*'*25)

segunda_carta_jugador = random.choice(cartas)

if segunda_carta_jugador == 'J' or segunda_carta_jugador == 'K' or segunda_carta_jugador == 'Q':
    segunda_carta_jugador = 10
elif segunda_carta_jugador == 'AS':
    segunda_carta_jugador = 11

palo_segunda_carta_jugador = random.choice(palos)

print('La carta de', player, 'es el numero', segunda_carta_jugador, 'cuyo palo es', palo_segunda_carta_jugador)

#Segunda Carta Croupier

segunda_carta_croupier = random.choice(cartas)

if segunda_carta_croupier == 'J' or segunda_carta_croupier == 'K' or segunda_carta_croupier == 'Q':
    segunda_carta_croupier = 10
elif segunda_carta_croupier == 'AS':
    segunda_carta_croupier = 11

palo_segunda_carta_croupier = random.choice(palos)

print('Segunda Carta Croupier: ',segunda_carta_croupier, 'palo', palo_segunda_carta_croupier)

#Puntajes Hasta Ahora

puntuacion_player = carta_jugador + segunda_carta_jugador
print('-'*25,'El puntaje total de', player, 'es de:', puntuacion_player, 'puntos','-'*25)

puntuacion_croupier = carta_croupier + segunda_carta_croupier
print('-'*25,'El puntaje total del croupieres de:', puntuacion_croupier, 'puntos','-'*25)


#Validamos el puntaje del croupier para saber si debe obtener una nueva carta, "el crupier está obligado a plantarse si suma 17 o más".

if puntuacion_croupier <= 17:
    print('No puede Recibir Mas Cartas')
    print('-' * 25, 'El puntaje total del croupieres de:', puntuacion_croupier, 'puntos', '-' * 25)
else:
    #En caso de que no se cumpla esa condicion el croupier esta habilitado a levantar una tercera carta
    tercera_carta_croupier = random.choice(cartas)

    if tercera_carta_croupier == 'J' or tercera_carta_croupier == 'K' or tercera_carta_croupier == 'Q':
        tercera_carta_croupier = 10
    elif tercera_carta_croupier == 'AS' and puntuacion_croupier < 21:
        tercera_carta_croupier = 11
#Mostramos el puntaje del croupier
puntuacion_croupier = carta_croupier + segunda_carta_croupier + tercera_carta_croupier
print('-'*25,'El puntaje total del croupieres de:', puntuacion_croupier, 'puntos','-'*25)

#El jugador no está obligado a seguir esas dos reglas, y puede plantarse cuando quiera o seguir pidiendo cartas mientras no sume 21, Validamos el puntaje del jugador para saber si puede obtener una tercera carta

if puntuacion_player > 21:
    print('No puede Recibir Mas Cartas')
    print('-' * 25, 'El puntaje total de', player, 'es de:', puntuacion_player, 'puntos', '-' * 25)

#Obtener puntuacion total

puntuacion_player = carta_jugador + segunda_carta_jugador
print('-'*25,'El puntaje total de', player, 'es de:', puntuacion_player, 'puntos','-'*25)

puntuacion_croupier = carta_croupier + segunda_carta_croupier
print('-'*25,'El puntaje total del croupieres de:', puntuacion_croupier, 'puntos','-'*25)
