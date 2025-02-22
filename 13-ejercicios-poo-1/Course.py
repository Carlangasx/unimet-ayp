from typing import List
from CourseClass import CourseClass
class Course:

  def __init__(self, title: str, code: str):
    self.title = title
    self.code = code
    self.class_courses: List[CourseClass] = []

  def append_class(self, class_course: CourseClass):
    self.class_courses.append(class_course)

  def __str__(self):
    return f'{self.code} - {self.title}'
