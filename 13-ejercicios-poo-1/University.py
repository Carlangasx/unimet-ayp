from typing import List
from Course import Course
from Student import Student
from Professor import Professor
from CourseClass import CourseClass
from Inscription import Inscription

class University:

  def __init__(self):
    self.courses: List[Course] = []
    self.students: List[Student] = []
    self.professors: List[Professor] = []

  def create_user(self, user_type: str):
    first_name = input('Por favor ingrese su nombre: ')
    last_name = input('Por favor ingrese su apellido: ')
    email = input('Por favor ingrese su correo: ')
    user = None
    if user_type == 'professor':
      user = Professor(first_name, last_name, email)
      self.professors.append(user)
    elif user_type == 'student':
      user = Student(first_name, last_name, email)
      self.students.append(user)
    return user

  # Crear profesor
  def create_professor(self):
    return self.create_user('professor')

  # Crear estudiante
  def create_student(self):
     return self.create_user('student')

  def search_user(self, email: str, user_type: str):
    user = None
    if user_type == 'professor':
      for professor in self.professors:
        if professor.email == email:
          user = professor
          break
    elif user_type == 'student':
      for student in self.students:
        if student.email == email:
          user = student
          break
    return user



  # Agregar materia y sus secciones
  def create_courses_and_classes(self):
    title = input('Por favor ingrese el título: ')
    code = input('Por favor ingrese el código: ')
    course = Course(title, code)
    # Secciones
    amount = int(input('Cuantas secciones desea agregar?: '))
    for num in range(1, amount + 1):
      schedule = input('Por favor ingrese un horario')
      course.append_class(CourseClass(num, schedule))
    self.courses.append(course)
    return course

  # Mostrar materias y sus secciones
  def show_courses_and_classes(self, show_classes: bool):
    for idx, course in enumerate(self.courses):
      print(f'{idx}. {course}')
      if show_classes:
        for class_course in course.class_courses:
          print(class_course)

  # Profesor puede agregar mas clases que dicta (selecciona una materia)
  def add_course_to_professor(self, professor: Professor):
    self.show_courses_and_classes(False)
    idx = int(input('Por favor ingrese el numero de la materia: '))
    course = self.courses[idx]
    professor.append_course(course)

  # Estudiante puede inscribir materias (crear una inscripción)
  def add_class_to_student(self, student: Student):
    period = input('Por favor ingresa el trimestre a inscribir: ')
    class_courses: List[CourseClass] = []
    ans = 'y'
    while ans == 'y':
      self.show_courses_and_classes(True)
      course_idx = int(input('Por favor ingresa el numero de la materia: '))
      class_idx = int(input('Por favor ingresa el indice de la sección: ')) - 1
      class_course = self.courses[course_idx].class_courses[class_idx]
      class_courses.append(class_course)
      ans = input('Deseas continuar? (y/n): ').lower()
    inscription = Inscription(period, class_courses)
    student.append_inscription(inscription)

  def menu(self):
    ans = 'y'
    while ans == 'y':
      option = input('''
        1. Registrar profesor
        2. Registrar estudiante
        3. Agregar materia al profesor
        4. Inscribir materia al estudiante
      ''')

      if option == '1':
        self.create_professor()
      elif option == '2':
        self.create_student()
      elif option == '3':
        # Buscar al professor
        email = input('Por favor ingrese su correo: ')
        professor = self.search_user(email, 'professor')
        if isinstance(professor, Professor):
          self.add_course_to_professor(professor)
        else:
          print('Error...')
      elif option == '4':
        # Buscar estudiante
        email = input('Por favor ingrese su correo: ')
        student = self.search_user(email, 'student')
        if isinstance(student, Student):
          self.add_class_to_student(student)
        else:
          print('Error...')
    ans = input('Desea continuar (y/n)?: ').lower()

