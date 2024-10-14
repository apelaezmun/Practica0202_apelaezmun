#Escribir un programa que pregunte el nombre del usuario en la consola y un
#número entero e imprima por pantalla en líneas distintas el nombre del
#usuario tantas veces como el número introducido.
Nombre = input('Escribe un nombre:')
Numero = int(input('Dime un numero entero:'))
print((Nombre + '\n') * Numero)