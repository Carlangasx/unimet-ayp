from typing import List
import time
# Modelar o hacer el sistema de un banco

def create_client(dni):
  # Pedir los datos del cliente
  first_name = input('Por favor ingrese su nombre: ').title()
  last_name = input('Por favor ingrese su apellido: ').title()
  address = input('Por favor ingrese su dirección: ')
  phone = input('Por favor ingrese su teléfono: ')
  # Crear el cliente
  client = {
    "first_name": first_name,
    "last_name": last_name,
    "address": address,
    "phone": phone,
    "dni": dni,
    "accounts": []
  }
  # Pedir los datos de la cuenta a crear
  account = create_account(len(client["accounts"]) + 1)
  client["accounts"].append(account)
  # retornar el valor del cliente nuevo
  return client

def create_account(number):
  account_type = input('Por favor diga si es ahorro o corriente: ')
  initial_amount = float(input('Por favor ingrese el deposito inicial: '))
  # opening_date = input('Por ingrese la fecha de hoy en formato dd/mm/yy: ')
  opening_date = time.strftime("%d/%m/%y")

  # Crear la cuenta
  account = {
    "number": number,
    "type": account_type,
    "balance": initial_amount,
    "opening_date": opening_date
  }
  return account

def admin_access(menu_admin, clients):
  option = int(input(menu_admin))
  if option == 5:
    sum_balances = 0
    for client in clients:
      client_balance = 0
      for account in client["accounts"]:
        client_balance += account["balance"]
        sum_balances += account["balance"]
      print(f'{client["dni"]}: {client_balance}')
    print(f'El total de los balances de los clientes es: {sum_balances}')

def search_client(dni: str, clients: List[dict]):
  client = None
  for registerClient in clients:
    if registerClient["dni"] == dni:
      client = registerClient
      break
  return client

def search_account(client):
  current_account = None
  if len(client["accounts"]) > 1:
    for act in client["accounts"]:
      print(f'{act["number"]} - {act["type"]} - {act["opening_date"]}')
    idx = int(input("Por favor ingresa el número de cuenta: "))
    current_account = client["accounts"][idx-1]
  else:
    current_account = client["accounts"][0]
  return current_account

def deposit(current_account):
  amount = float(input('Por favor ingrese un monto: '))
  current_account["balance"] += amount
  print(f'El nuevo balance disponible es: {current_account["balance"]}')

def withdraw(current_account):
  amount = float(input('Por favor ingrese un monto: '))
  if amount < current_account["balance"]:
    current_account["balance"] -= amount
    print(f'El nuevo balance disponible es: {current_account["balance"]}')
  else:
    print('Error el monto a retirar mas del disponible')

def loan(current_account):
  # Hacer un prestamos
  # Como maximo del 30% del saldo disponible
  amount = float(input('Ingrese el monto a solicitar: '))
  max_amount = current_account["balance"] * (30/100)

  if amount <= max_amount:
    time = 12 # months
    interest_rate = 16 / 100
    interest = amount * ((1 + interest_rate/time) ** time) - amount
    monthly_payments = (amount + interest) / time
    print(f'El prestamo debera pagarse mensualmente con un cuota de {monthly_payments}')
  else:
    print('No tienes suficiente dinero para fondear el prestamo!')

def user_access(menu, clients):
  dni = input('Por favor ingrese una cédula: ')
  # este es el caso de un cliente nuevo del banco
  client = search_client(dni, clients)
  if client == None:
    client = create_client(dni)
    clients.append(client)

  # Buscar la cuenta para trabajar
  current_account = search_account(client)
  option = int(input(menu))
  OPTIONS = {
    'CHECK_BALANCE': 0,
    'DEPOSIT': 1,
    'WITHDRAW': 2,
    'LOAN': 3,
    'OPEN_ACCOUNT': 4
  }

  if option == OPTIONS['CHECK_BALANCE']:
    print(f'El balance disponible es: {current_account["balance"]}')
  elif option == OPTIONS['DEPOSIT']:
    deposit(current_account)
  elif option == OPTIONS['WITHDRAW']:
    withdraw(current_account)
  elif option == OPTIONS['LOAN']:
    loan(current_account)
  elif option == OPTIONS['OPEN_ACCOUNT']:
    account = create_account(len(client["accounts"]) + 1)
    client["accounts"].append(account)
