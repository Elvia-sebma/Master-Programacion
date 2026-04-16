# Generador ID Unico
from random import randint

print('*** Sistema de Generador ID Unico ***')

nombre = input('Ingresa tu nombre: ')
nombre_2 = nombre[0:2].upper()

apellido = input('Ingresa tu primer apellido: ')
apellido_2 = apellido[0:2].upper()

anio_de_nacimiento =input('Ingresa tu año de nacimiento (YYYY): ')
anio_de_nacimiento2 = anio_de_nacimiento[2:4]

#Generador un valor de 4 digitos aleatorio
aleatorio = randint(0,9999)

#Generamos el ID Unico
#id_unico = nombre_2 + apellido_2 + anio_de_nacimiento + str(aleatorio)
id_unico = f'{nombre_2}{apellido_2}{anio_de_nacimiento2}{aleatorio}'
#print(id_unico)
print(f'''\nHola{nombre},habitante de ciudad gotica!
        Tu numero de identificacion (ID) generado por el sistema es
        {id_unico}
        Felicidades!''')
