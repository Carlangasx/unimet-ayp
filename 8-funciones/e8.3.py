import typing

def main():
    class Paciente:
        def __init__(self, cedula:int, nombre:str, apellido:str, telefono:int, razon:str):
            self.cedula = cedula
            self.nombre = nombre
            self.apellido = apellido
            self.telefono = telefono
            self.razon = razon
    #llenado de datos
    data_headers:list = ['cedula', 'nombre', 'apellido', 'telefono', 'razon']
    paciente1:Paciente
    for i in data_headers:
        paciente1.i = input(f'Ingrese su {i}:')
    #def fillin_data() -> Paciente:
       # name = input
        

  

main()
