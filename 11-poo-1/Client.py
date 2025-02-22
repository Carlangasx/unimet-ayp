from typing import List
from Account import Account
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
    account = Account(str(number), type, opening_balance, date)
    self.accounts.append(account)
    return account

  def ask_for_loan(self, account: Account):
    amount = float(input('Por favor ingrese el monto a solicitar: '))
    TIME_IN_MONTHS = 12
    INTEREST_RATE = 16.0 / 100 # % tasa de interes lleva a fracción
    loan = Loan.create(account.balance, amount, TIME_IN_MONTHS, INTEREST_RATE)
    print(f'El prestamo debera pagarse mensualmente con un cuota de {loan.monthly_payments}')

