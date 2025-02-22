from typing import List

students: List[str] = ['Jose Roberto', 'Luis Eduardo', 'Antonio']

ans = 'y'

while ans == 'y':
  name = input('Por favor ingrese un nombre: ')
  students.append(name)
  ans = input('Desea continuar? (y/n): ').lower()

print(students)
usernames: List[str] = []

for student in students:
  usernames.append(student.lower().replace(' ', '_'))

print(usernames)

