#Generador ID Unico
from random import randint
print('*** Sistema de Generador ID Unico ***')
nombre = input('Cual es tu Nombre?')
nombre_2 =nombre[0:2].upper()
#print(nombre_2)
apellido = input('Cual es tu Apellido?')
apellido_2 = apellido[0:2].upper()
#print(apellido_2)
anio =input('Cual es tu Año de Nacimiento(YYYY)?')
anio_2 = anio[2:4]

#Generar un valor de 4 digitos aleatoria
aleatorio = randint(0,9999)
#print(aleatorio)
#Generamos el ID Unico
#id_unico =nombre_2 + apellido_2 + anio_2 + str(aleatorio)
id_unico=f'{nombre_2}{apellido_2}{anio_2}{aleatorio}'
#print(id_unico)

print(f'''\nHola {nombre},habitante de ciudad gotica!
    Tu nuevo numero de identificacion (ID) generado por el sistema es:
    {id_unico}
    Felicidades!''')
