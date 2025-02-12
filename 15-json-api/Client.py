from typing import List, Dict
from Account import Account
from CheckingAccount import CheckingAccount
from SavingAccount import SavingAccount
from Loan import Loan
class Client:

  def __init__(self, first_name: str, last_name: str, address: str, phone: str, dni: str):
    self.first_name = first_name
    self.last_name = last_name
    self.address = address
    self.phone = phone
    self.dni = dni
    self.accounts: List[Account] = []
    self.loans: List[Loan] = []

  def open_account(self, type: str, opening_balance: float, date: str):
    number = len(self.accounts) + 1
    account = None
    if (type == 'corriente'):
      account = CheckingAccount(str(number), opening_balance, date)
    else:
      account = SavingAccount(str(number), opening_balance, date)
    self.accounts.append(account)
    return account

  def ask_for_loan(self, account: Account):
    amount = float(input('Por favor ingrese el monto a solicitar: '))
    TIME_IN_MONTHS = 12
    INTEREST_RATE = 16.0 / 100 # % tasa de interes lleva a fracción
    loan = Loan.create(account.balance, amount, TIME_IN_MONTHS, INTEREST_RATE)
    print(f'El prestamo debera pagarse mensualmente con un cuota de {loan.monthly_payments}')


  def to_dict(self):
    result = {
      'first_name': self.first_name,
      'last_name': self.last_name,
      'address': self.address,
      'phone': self.phone,
      'dni': self.dni,
      'accounts': [],
      'loans': [],
    }
    for acc in self.accounts:
      result['accounts'].append(acc.to_dict())
    for loan in self.loans:
      result['loans'].append(loan.to_dict())
    return result


  def from_dict(dict: Dict[str, any]):
    client = Client(dict.get('first_name'), dict.get('last_name'), dict.get('address'), dict.get('phone'), dict.get('dni'))
    # Agregar cuentas
    for acc in dict.get('accounts', []):
      if acc.get('account_type') == 'corriente':
        client.accounts.append(CheckingAccount(acc.get('number'), acc.get('balance'), acc.get('date')))
      elif acc.get('account_type') == 'ahorro':
        client.accounts.append(SavingAccount(acc.get('number'), acc.get('balance'), acc.get('date')))
    # Agregar prestamos
    for loan in dict.get('loans', []):
      client.loans.append(Loan.recreate(
        loan.get('amount', 0),
        loan.get('time', 1),
        loan.get('interest_rate', 0),
        loan.get('interest', 0),
        loan.get('monthly_payments', 0),
      ))
    return client
