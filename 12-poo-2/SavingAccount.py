from Account import Account

class SavingAccount(Account):

  def __init__(self, number: str, opening_balance: float, date: str):
    super().__init__(number, opening_balance, date)


  def deposit(self, amount: float):
    self.balance = (self.balance + amount) * 1.03
    return self.balance

  def account_type(self):
    return 'ahorro'
