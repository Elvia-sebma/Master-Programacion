# Menu interactivo con ciclo while
print('***Sistema de Administracion de Cuentas')
salir = False
while not salir:
    print(f'''Menu:
        1.Crear cuenta
        2.Eliminar cuenta
        3.Salir
    ''')
    opcion =int( input('Escoje una opccion:'))
    if opcion == 1 :
        print('Creando tu cuenta ...\n')
    elif opcion == 2 :
        print('Eliminando tu cuenta')
    elif opcion == 3 :
        print('Saliendo del sistema, Hasta pronto...\n')
        salir = True
    else :
        print('Opcion invalida, selecciona otra opccion')


