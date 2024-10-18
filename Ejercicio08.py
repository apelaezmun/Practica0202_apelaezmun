#Escribir un programa que pregunte por consola el precio de un producto en
#euros con dos decimales y muestre por pantalla el número de euros y el
#número de céntimos del precio introducido.
Precio = input('Precio del producto (€) con dos decimales:')
Precio = Precio.split('.')
print(Precio[0], 'euros ,', Precio[1], 'centimos')