from typing import List
from Professor import Professor
from Student import Student

class CourseClass:

  def __init__(self, number: int, schedule: str):
    self.number = number
    self.schedule = schedule
    self.professor: Professor = None
    self.students: List[Student] = []

  def __str__(self):
    return '{self.number} - {self.schedule}'

