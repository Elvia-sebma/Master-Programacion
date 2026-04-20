print('*** Operador Logico and ***')
condicion1 = True
condicion2 = True
#Aplicamos el operador and
resultado = condicion1 and condicion2

#print(f'Resultado {condicion1} and {condicion2} : {resultado}')

#El operador and si cualquiera de sus operandos
# es falso toda la expresion regresa falso

#Ejemplo if else con operador and
llueve = False
nublado = False
print(f'\n Revison del clima')
if llueve and nublado :
    print('Llevar paraguas e impermeable, llueve y esta nublado')
elif llueve :
    print('Llevar paraguas, va a llover')
elif nublado :
    print('Llevar impermeable, solo esta nublado')
else:
    print('Dejar paraguas e impermeable ,disfruta de tu dia')
