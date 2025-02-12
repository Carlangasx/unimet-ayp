from typing import List
# Modelar o hacer el sistema de un banco

clients: List[dict] = [
  {
    'first_name': 'Jose',
    'last_name': 'Quevedo',
    'address': 'Los naranjos',
    'phone': '04121111111',
    'dni': '27014788',
    'accounts': [
      {'number': 1, 'type': 'corriente', 'balance': 100.0, 'opening_date': '25/09/24'},
      {'number': 2, 'type': 'ahorro', 'balance': 1000000.0, 'opening_date': '25/09/24'},
      {'number': 3, 'type': 'corriente', 'balance': 500.0, 'opening_date': '25/09/24'}
    ]
  },
  {
    'first_name': 'Ivanna',
    'last_name': 'Padron',
    'address': 'Los naranjos',
    'phone': '04141111111',
    'dni': '23828274',
    'accounts': [
      {'number': 1, 'type': 'corriente', 'balance': 1000.0, 'opening_date': '23/09/24'}
    ]
  },
  {
    'first_name': 'Luis',
    'last_name': 'Bello',
    'address': 'El marquez',
    'phone': '04241111111',
    'dni': '23871097',
    'accounts': [
      {'number': 1, 'type': 'ahorro', 'balance': 10000.0, 'opening_date': '25/09/22'},
      {'number': 2, 'type': 'corriente', 'balance': 150.0, 'opening_date': '25/09/23'}
    ]
  }
]

# Hacer un menu

menu = """
  0. CONSULTAR BALANCE
  1. DEPOSITAR
  2. RETIRAR
  3. SOLICITAR PRESTAMO -> NOTA: Solo se podra prestar el 30% del saldo disponible
  4. CREAR CUENTA
"""

menu_admin = """
  5. [ADMINISTRADOR]: Balances disponibles
"""

SECRET_CODE = '-999'

ans = 'y'

while ans == 'y':

  access_code = input('Ingrese su codigo de acceso: ')

  if access_code == SECRET_CODE:
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
  else:

    dni = input('Por favor ingrese una cédula: ')

    client = None

    for registerClient in clients:
      if registerClient["dni"] == dni:
        client = registerClient
        break

    # este es el caso de un cliente nuevo del banco
    if client == None:
      first_name = input('Por favor ingrese su nombre: ').title()
      last_name = input('Por favor ingrese su apellido: ').title()
      address = input('Por favor ingrese su dirección: ')
      phone = input('Por favor ingrese su teléfono: ')

      client = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "phone": phone,
        "dni": dni,
        "accounts": []
      }

      clients.append(client)

      number = len(client["accounts"]) + 1
      account_type = input('Por favor diga si es ahorro o corriente: ')
      initial_amount = float(input('Por favor ingrese el deposito inicial: '))
      opening_date = input('Por ingrese la fecha de hoy en formato dd/mm/yy: ')
      account = {
        "number": number,
        "type": account_type,
        "balance": initial_amount,
        "opening_date": opening_date
      }

      client["accounts"].append(account)

    # Buscar la cuenta para trabajar
    current_account = None

    if len(client["accounts"]) > 1:
      for act in client["accounts"]:
        print(f'{act["number"]} - {act["type"]} - {act["opening_date"]}')
      idx = int(input("Por favor ingresa el número de cuenta: "))
      current_account = client["accounts"][idx-1]
    else:
      current_account = client["accounts"][0]

    option = int(input(menu))

    if option == 0:
      print(f'El balance disponible es: {current_account["balance"]}')
    elif option == 1:
      amount = float(input('Por favor ingrese un monto: '))
      current_account["balance"] += amount
      print(f'El nuevo balance disponible es: {current_account["balance"]}')
    elif option == 2:
      amount = float(input('Por favor ingrese un monto: '))
      if amount < current_account["balance"]:
        current_account["balance"] -= amount
        print(f'El nuevo balance disponible es: {current_account["balance"]}')
      else:
        print('Error el monto a retirar mas del disponible')
        break
    elif option == 3:
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

    elif option == 4:
      number = len(client["accounts"]) + 1
      account_type = input('Por favor diga si es ahorro o corriente: ')
      initial_amount = float(input('Por favor ingrese el deposito inicial: '))
      opening_date = input('Por ingrese la fecha de hoy en formato dd/mm/yy: ')
      account = {
        "number": number,
        "type": account_type,
        "balance": initial_amount,
        "opening_date": opening_date
      }
      client["accounts"].append(account)

  ans = input('Desea continuar? (y/n): ').lower()
