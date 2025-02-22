class Worker:

  def __init__(self, first_name: str, last_name: str, dni: str):
    self.first_name = first_name
    self.last_name = last_name
    self.dni = dni

  def __str__(self):
    return f'{self.first_name} {self.last_name} - {self.dni}'


  def get_hourly_rate(self) -> int:
    pass
