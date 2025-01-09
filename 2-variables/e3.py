
name:str = input('Nombre completo: ')
birth_date = input('¡Excelente! Año de nacimiento: ')

age:int = 2025 - int(birth_date)

print(f'{name} debe cumplir o cumplió {int(age)} este año')