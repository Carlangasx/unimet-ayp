from Account import Account

class CheckingAccount(Account):

  def __init__(self, number: str, opening_balance: float, date: str):
    super().__init__(number, opening_balance, date)

  def deposit(self, amount: float):
    self.balance += amount
    return self.balance

  def account_type(self):
    return 'corriente'

