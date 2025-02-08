import typing

def main():
    path = input('Enter the path: ')

    def its_crossed(route:str) -> bool:

        #inicializar variables
        x:int = 0
        y:int = 0
        posicion:tuple = (0, 0)
        log:list = []

        #definir estado inicial
        posicion = (x, y)
        log.append(posicion)

        #recorrer la ruta
        for i in route:
            match i:
                case 'N':
                    y += 1
                case 'S':
                    y -= 1
                case 'E':
                    x += 1
                case 'W':
                    x -= 1
                case _: pass
            #actualizar posicion
            posicion = (x, y)
            #verificar si se ha cruzado
            if posicion in log:
                print('The path is crossed')
                return True #Se han cruzado            
           #actualizar el registro
            log.append(posicion)
    
        return False #No se han cruzado
    print(its_crossed(path))

main()

            
