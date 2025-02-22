from User import User
from typing import List
from Course import Course

class Professor(User):

  def __init__(self, first_name: str, last_name: str, email: str):
    super().__init__(first_name, last_name, email)
    self.courses: List[Course] = []

  def append_course(self, course: Course):
    self.courses.append(course)
