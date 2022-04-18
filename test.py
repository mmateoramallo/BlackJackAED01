contador = 1
numero = int(input('Ingrese un numero: '))

print('La tabla del', numero , 'es: ')

while contador <= 10:

    print(numero, "x", contador,'=' ,str(numero * contador))

    contador = contador + 1
