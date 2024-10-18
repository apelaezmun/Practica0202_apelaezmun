#Escribir un programa que pregunte al usuario la fecha de su nacimiento en
#formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar
#el programa anterior para que también funcione cuando el día o el mes
#se introduzcan con un solo carácter.
Fecha = input('Escribe tu fecha de tu nacimiento (dd/mm/aaaa):')
Fecha = Fecha.split('/')
print('Dia', Fecha[0])
print('Mes', Fecha[1])
print('Año', Fecha[2])