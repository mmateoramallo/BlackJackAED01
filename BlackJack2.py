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

palo_primera_carta_jugador = random.choice(palos)

if carta_jugador == 'J' or carta_jugador == 'K' or carta_jugador == 'Q':
    carta_jugador_letra = carta_jugador
    carta_jugador = 10
    print('La carta de', player, 'es la', carta_jugador_letra, 'cuyo palo es', palo_primera_carta_jugador)
elif carta_jugador == 'AS':
    carta_jugador_letra = carta_jugador
    carta_jugador = 11
    print('La carta de', player, 'es el', carta_jugador_letra, 'cuyo palo es', palo_primera_carta_jugador)

print('La carta de', player, 'es el numero', carta_jugador, 'cuyo palo es', palo_primera_carta_jugador)

#Primera Carta Croupier

carta_croupier = random.choice(cartas)

palo_primera_carta_croupier = random.choice(palos)

if carta_croupier == 'J' or carta_croupier == 'K' or carta_croupier == 'Q':
    carta_croupier_letra = carta_croupier
    carta_croupier = 10
    print('Carta Croupier: ', carta_croupier_letra, 'cuyo palo es', palo_primera_carta_croupier)
elif carta_croupier == 'AS':
    carta_croupier_letra = carta_croupier
    carta_croupier = 11
    print('Carta Croupier:', carta_croupier_letra, 'de', palo_primera_carta_croupier)

print('Carta Croupier: ', carta_croupier, 'palo' , palo_primera_carta_croupier)

#Puntaje De Ambos Jugadores

puntuacion_player = carta_jugador

print('-'*25,'El puntaje total de', player, 'es de:', puntuacion_player, 'puntos','-'*25)

puntuacion_croupier = carta_croupier

print('-'*25,'El puntaje total del croupier es de:', puntuacion_croupier, 'puntos','-'*25)


#----------------------------------------------------#
#Segunda Mano De Cartas

print('*'*25, 'Generando Segunda Tirada', '*'*25)

segunda_carta_jugador = random.choice(cartas)

palo_segunda_carta_jugador = random.choice(palos)

if segunda_carta_jugador == 'J' or segunda_carta_jugador == 'K' or segunda_carta_jugador == 'Q':
    carta_jugador_letra = segunda_carta_jugador
    segunda_carta_jugador = 10
    print('La carta de', player, 'es la', carta_jugador_letra, 'cuyo palo es', palo_segunda_carta_jugador)
elif segunda_carta_jugador == 'AS':
    carta_jugador_letra = segunda_carta_jugador
    segunda_carta_jugador = 11
    print('La carta de', player, 'es el', carta_jugador_letra, 'cuyo palo es', palo_segunda_carta_jugador)


print('La carta de', player, 'es el numero', segunda_carta_jugador, 'cuyo palo es', palo_segunda_carta_jugador)

#Segunda Carta Croupier

segunda_carta_croupier = random.choice(cartas)

palo_segunda_carta_croupier = random.choice(palos)

if segunda_carta_croupier == 'J' or segunda_carta_croupier == 'K' or segunda_carta_croupier == 'Q':
    carta_croupier_letra = segunda_carta_croupier
    segunda_carta_croupier = 10
    print('Carta Croupier: ', carta_croupier_letra, 'cuyo palo es', palo_segunda_carta_croupier)
elif segunda_carta_croupier == 'AS':
    carta_croupier_letra = segunda_carta_croupier
    segunda_carta_croupier = 11
    print('Carta Croupier:', carta_croupier_letra, 'de', palo_segunda_carta_croupier)



print('Segunda Carta Croupier: ',segunda_carta_croupier, 'palo', palo_segunda_carta_croupier)

#Puntajes Hasta Ahora

puntuacion_player = carta_jugador + segunda_carta_jugador
print('-'*25,'El puntaje total de', player, 'es de:', puntuacion_player, 'puntos','-'*25)

puntuacion_croupier = carta_croupier + segunda_carta_croupier
print('-'*25,'El puntaje total del croupier es de:', puntuacion_croupier, 'puntos','-'*25)

#--------------------------> Tercera Carta, Validacion

print('*'*25, 'Generando Tercera Tirada', '*'*25)

#Obtencion De Tercera Carta Para el jugador

if puntuacion_player < 21:

    tercera_carta_jugador = random.choice(cartas)


if puntuacion_croupier <= 16:
    if puntuacion_croupier >= 17:
        print('Fin de la Mano Para el Croupier')

    tercera_carta_croupier = random.choice(cartas)

    palo_tercera_carta_croupier = random.choice(palos)

    if tercera_carta_croupier == 'J' or tercera_carta_croupier == 'K' or tercera_carta_croupier == 'Q':
        carta_croupier_letra = tercera_carta_croupier
        tercera_carta_croupier = 10
        print('Carta Croupier: ', carta_croupier_letra, ' cuyo palo es' , palo_tercera_carta_croupier)
    elif tercera_carta_croupier == 'AS':
        carta_croupier_letra = tercera_carta_croupier
        tercera_carta_croupier = 11
        print('Carta Croupier: ', carta_croupier_letra, 'de', palo_tercera_carta_croupier)

    print('Tercera Carta Croupier:', tercera_carta_croupier, 'palo', palo_tercera_carta_croupier)





#Obtener puntuacion total

print()
print()
print()

puntuacion_player = carta_jugador + segunda_carta_jugador
print('-'*25,'El puntaje total de', player, 'es de:', puntuacion_player, 'puntos','-'*25)

puntuacion_croupier = carta_croupier + segunda_carta_croupier
print('-'*25,'El puntaje total del croupier es de:', puntuacion_croupier, 'puntos','-'*25)
