class Account:

  def __init__(self, number: str, opening_balance: float, date: str):
    self.number = number
    if opening_balance < 0:
      opening_balance = 0
    self.balance = opening_balance
    self.date = date

  def balance_check(self):
    return self.balance

  # Método abstracto
  def deposit(self, amount: float) -> float:
    pass

  def withdraw(self, amount: float):
    if self.balance < amount:
      raise Exception("No se puede retirar más dinero del disponible")
    self.balance -= amount
    return self.balance


  def account_type(self):
    return ''
