class Loan:

  def create(balance: float, amount: float, time_in_months: int, interest_rate: float):
    MAX_THRESOLD = 30 / 100 # 30%
    max_amount = balance * MAX_THRESOLD
    if amount <= max_amount:
      return Loan(amount, time_in_months, interest_rate)
    raise Exception(f"No se puede prestar más del {MAX_THRESOLD*100}% del balance disponible")


  def recreate(amount: float, time: int, interest_rate: float, interest: float, monthly_payments: float):
    loan = Loan(0, 1, 0)
    loan.amount = amount
    loan.time = time
    loan.interest_rate = interest_rate
    loan.interest = interest
    loan.monthly_payments = monthly_payments
    return loan

  def __init__(self, amount: float, time_in_months: int, interest_rate: float):
    self.amount = amount
    self.time = time_in_months
    self.interest_rate = interest_rate
    self.interest = amount * ((1 + self.interest_rate/self.time) ** self.time) - amount
    self.monthly_payments = (self.amount + self.interest) / self.time


  def to_dict(self):
    return {
      'amount': self.amount,
      'time': self.time,
      'interest_rate': self.interest_rate,
      'interest': self.interest,
      'monthly_payments': self.monthly_payments,
    }
