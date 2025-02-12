from User import User
from typing import List
from Inscription import Inscription

class Student(User):

  def __init__(self, first_name: str, last_name: str, email: str):
    super().__init__(first_name, last_name, email)
    self.inscriptions: List[Inscription] = []


  def append_inscription(self, inscription: Inscription):
    self.inscriptions.append(inscription)
