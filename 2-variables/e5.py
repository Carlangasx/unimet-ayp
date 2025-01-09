import typing 

k: float = 8.85e-12

while True:
    datos:str = input('Datos en la forma: q1 q2 r .SIN Espacios: ')
    if (len(datos) == 5):
        q1:float = int(datos[0])
        q2:float = int(datos[2])
        r:float = int(datos[4])
        break

magnitud:float = k * (q1 * q2) / (r**2) 


print(f'Magnitud: {magnitud}')


