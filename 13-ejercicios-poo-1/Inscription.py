from typing import List
from CourseClass import CourseClass

class Inscription:

  def __init__(self, period: str, class_courses: List[CourseClass]):
    self.period = period
    self.class_courses = class_courses
