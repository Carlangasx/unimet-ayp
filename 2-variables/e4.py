while True:
    datos:str = input('Lados del triangulo en la forma ABC: ') 
    if((len(datos) == 3)):
        a = int(datos[0])
        b = int(datos[1])
        c = int(datos[2])
        break
# s para semiperímetro de un triángulo
s:float = (a+b+c)/(2)

# fórmula de Herón para el area de un triángulo
area:float = (s*(s-a)*(s-b)*(s-c))**(1/2)

print(f'El área del tringulo es {area} cm')