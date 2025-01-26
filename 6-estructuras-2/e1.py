import typing

#inicializar las listas corresponietes
label_list: list = []
coordenadas_list: list = ['x','y','z']
n: int = 1

while True:
    #solicitud de información al usuario
    label = input("Ingrese la etiqueta del punto: ")
    coordenadas = input("Ingrese las coordenadas de la forma 'x,y,z': ")

     #separar coordenadas en sus ejes correspondientes
    coordenadas = coordenadas.split(',')
    
    x = coordenadas[0]
    y = coordenadas[1]
    z = coordenadas[2]

    print(f'{label}: {x}, {y}, {z}')
    respuesta = input('Agregar otra coordenada? (y/n): ')
    if respuesta == n:
        break
    else:
        continue
        