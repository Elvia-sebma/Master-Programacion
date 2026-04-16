print('*** Bienvenido al  Sistema de generacion  de Email de Ciudad Gotica ***')

nombre =input('Cual es tu nombre?: ')
#nombre = nombre.lower()

apellido = input('Cual es tu apellido?: ')
#apellido = apellido.lower()

# Generamos el Email
email_generado = f'{nombre.lower()}.{apellido.lower()}@ciudadgotica.com'
print(email_generado)
print(f'''
Tu nuevo email generado por el sistema es:
        {email_generado}
        *** Felicidades ***
''')


