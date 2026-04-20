#Generador de email

print('***Bienvenido al sistema de generacion de email de ciudad gotica ***')
nombre =input('¿Cual es tu nombre?')
nombre_2=nombre[0:10].lower()

#print(nombre_2)

apellido =input('¿Cual es tu apellido?')
apellido_2=apellido[0:10].lower()

#print(apellido_2)
punto=('.')
ciudad=('@ciudadgotica.com')
#print(punto)
#Generamos el Email
email=f'{nombre_2}{punto}{apellido_2}{ciudad}'
#print(email)

print(f'''\nTu nuevo email generado por el sistema es:
    {email}
    Felicidades!''')

