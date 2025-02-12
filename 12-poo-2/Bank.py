from typing import List
from Client import Client
from CheckingAccount import CheckingAccount
from SavingAccount import SavingAccount
import time

class Bank:

  def __init__(self):
    self.clients: List[Client] = [
      Client("Jose", "Quevedo", "Los Naranjos", "04121111111", "27014788")
    ]
    self.clients[0].open_account("ahorro", 100.0, time.strftime("%d/%m/%y"))

  def create_client(self, dni: str):
    first_name = input('Por favor ingrese su nombre: ').title()
    last_name = input('Por favor ingrese su apellido: ').title()
    address = input('Por favor ingrese su dirección: ')
    phone = input('Por favor ingrese su teléfono: ')
    client = Client(first_name, last_name, address, phone, dni)
    self.open_account(client)
    return client

  def search_client(self, dni: str):
    client = None
    for registerClient in self.clients:
      if registerClient.dni == dni:
        client = registerClient
        break
    return client

  def search_account(self, client: Client):
    current_account = None
    if len(client.accounts) > 1:
      for act in client.accounts:
        account_type = ''

        if isinstance(act, CheckingAccount):
          account_type = 'corriente'
        elif isinstance(act, SavingAccount):
          account_type = 'ahorro'

        print(f'{act.number} - {account_type} - {act.date}')
      idx = int(input("Por favor ingresa el número de cuenta: "))
      current_account = client.accounts[idx-1]
    else:
      current_account = client.accounts[0]
    return current_account

  def open_account(self, client: Client):
    account_type = input('Por favor diga si es ahorro o corriente: ')
    initial_amount = float(input('Por favor ingrese el deposito inicial: '))
    opening_date = time.strftime("%d/%m/%y")
    client.open_account(account_type, initial_amount, opening_date)

  def client_operations(self):
    dni = input('Por favor ingrese una cédula: ')
    # este es el caso de un cliente nuevo del banco
    client = self.search_client(dni)
    if client == None:
      client = self.create_client(dni)
      self.clients.append(client)

    # Buscar la cuenta para trabajar
    current_account = self.search_account(client)
    option = int(input("""
      0. CONSULTAR BALANCE
      1. DEPOSITAR
      2. RETIRAR
      3. SOLICITAR PRESTAMO -> NOTA: Solo se podra prestar el 30% del saldo disponible
      4. CREAR CUENTA
    """))
    OPTIONS = {
      'CHECK_BALANCE': 0,
      'DEPOSIT': 1,
      'WITHDRAW': 2,
      'LOAN': 3,
      'OPEN_ACCOUNT': 4
    }

    if option == OPTIONS['CHECK_BALANCE']:
      print(f'El balance disponible es: {current_account.balance_check()}')
    elif option == OPTIONS['DEPOSIT']:
      amount = float(input("Por favor ingrese el monto a depositar: "))
      new_balance = current_account.deposit(amount)
      print(f'El balance disponible es: {new_balance}')
    elif option == OPTIONS['WITHDRAW']:
      amount = float(input("Por favor ingrese el monto a depositar: "))
      new_balance = current_account.withdraw(amount)
      print(f'El balance disponible es: {new_balance}')
    elif option == OPTIONS['LOAN']:
      client.ask_for_loan(current_account)
    elif option == OPTIONS['OPEN_ACCOUNT']:
      self.open_account(client)

  def star(self):
    SECRET_CODE = '-999'

    ans = 'y'

    while ans == 'y':
      access_code = input('Ingrese su codigo de acceso: ')
      if access_code == SECRET_CODE:
        # admin_access(menu_admin, clients)
        pass
      else:
        self.client_operations()
      ans = input('Desea continuar? (y/n): ').lower()

bank = Bank()
bank.star()



