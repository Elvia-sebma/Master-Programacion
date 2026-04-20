print('***Calculadora***')
valor1 = 0 #Definimos las variables iniciales en 0
valo2 = 0
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1.-Suma
    2.-Resta
    3.-Multiplicacion
    4-.Division
    5.-Salir
''')
    opcion=int(input('Selecciona una operacion: '))
    if opcion == 1:#suma
        valor1=float(input('ingresa el primer valor:'))
        valor2=float(input('Ingresa el segundo valor:'))
        suma=valor1+valor2
        print(f'El resultado de la suma es:{suma}')
    elif opcion == 2:
        valor1 = float(input('ingresa el primer valor:'))
        valor2 = float(input('Ingresa el segundo valor:'))
        resta = valor1-valor2
        print(f'El resultado de la Resta es:{resta}')
    elif opcion == 3:
        valor1 = float(input('ingresa el primer valor:'))
        valor2 = float(input('Ingresa el segundo valor:'))
        multiplicacion = valor1 * valor2
        print(f'El resultado de la multiplicacion es:{multiplicacion}')
    elif opcion == 4:
        valor1 = float(input('ingresa el primer valor:'))
        valor2 = float(input('Ingresa el segundo valor:'))
        division = valor1 / valor2
        print(f'El resultado de la division es:{division}')

    elif opcion == 5:
        print('Saliendo de la calculador')
        salir=True
    else:
        print('opcion invalida,selccione otra opccion')


