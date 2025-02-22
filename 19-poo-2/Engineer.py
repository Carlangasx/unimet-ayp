from Worker import Worker
class Engineer(Worker):

  def __init__(self, first_name: str, last_name: str, dni: str, specialty: str):
    super().__init__(first_name, last_name, dni)
    self.speciality = specialty

  def get_hourly_rate(self):
    return 25
