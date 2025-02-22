from Worker import Worker
from utils import *

class Invoice:
  def __init__(self, worker: Worker, worked_hours: float, month: int, year: int):
    self.worker = worker
    self.worked_hours = worked_hours
    self.month = month
    self.year = year
    # subtotal
    self.subtotal = worker.get_hourly_rate() * worked_hours
    # recargos
    recharge = 0
    if is_prime(worked_hours):
      recharge = (self.subtotal) * 0.05
    if is_defficent(self.subtotal):
      recharge += self.subtotal * 0.1
    if worked_hours in get_factorial_set(worked_hours):
      recharge += self.subtotal * 0.15
    # total
    self.total = self.subtotal + recharge


  def __str__(self):
    return f'''
      FACTURA DE PAGO
      Fecha: {self.year}-{self.month}
      Worker: {self.worker.dni} - {self.worker.first_name} {self.worker.last_name} - {self.worker.specialty}
      ---------------------
      Sub total: {self.subtotal}
      Recargos: {self.total - self.subtotal}
      Total: {self.total}
    '''
