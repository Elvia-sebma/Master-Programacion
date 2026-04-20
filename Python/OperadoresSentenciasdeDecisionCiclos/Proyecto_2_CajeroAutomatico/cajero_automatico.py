print('*** Cajero Automatico de Ciudad Gotica***')

saldo = 1000 #Saldo inicial
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1.-Consultar Saldo
    2.-Retirar
    3.-Depositar
    4.-Salir
    ''')
    opcion = int(input('Escoje una opccion:'))
    if opcion == 1:
        print(f'Tu Saldo actual es: {saldo}')
    elif opcion == 2 :
        retiro = float(input('Ingrese el monto a retirar : '))
        #Validacion
        if retiro <= saldo:
            saldo -= retiro # Saldo = saldo -retiro
            print(f'Tu nuevo Saldo es : {saldo}')
        else:
            print(f'No cuentas con saldo suficiente. saldo actual{saldo}')
    elif opcion == 3 :
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito # saldo = saldo + deposito
        print(f'Tu nuevo saldo es:{saldo}')
    elif opcion == 4:
        print('saliendo del cajero automatico. Hasta pronto')
        salir = True

