from typing import List
# Modelar o hacer el sistema de un banco

accounts_balance: List[float] = [100, 500, 1000, 300, 360, 120]

# Hacer un menu

menu = """
0. CONSULTAR BALANCE
1. DEPOSITAR
2. RETIRAR
3. SOLICITAR PRESTAMO -> NOTA: Solo se podra prestar el 30% del saldo disponible
"""

menu_admin = """
  4. [ADMINISTRADOR]: Balances disponibles
"""

SECRET_CODE = -999

ans = 'y'

while ans == 'y':
  idx = int(input("Por favor ingresa el número de cuenta: "))

  if idx == SECRET_CODE:
    option = int(input(menu_admin))

  if idx < 0 and idx != SECRET_CODE:
    print('Error: Debe dar un numero de cuenta positivo!')
    break

  if idx > len(accounts_balance):
    # Esto es la apertura de cuenta
    accounts_balance.append(0)
    idx = len(accounts_balance) - 1
    print(f"Tu numero de cuenta: {idx}")

  account_balance: float = 0

  if idx != SECRET_CODE:
    account_balance = accounts_balance[idx]
    option = int(input(menu))

  if option == 0:
    print(f"El balance disponible es: {account_balance}")
  elif option == 1:
    # 1. Depositar
    amount = float(input("Por favor ingrese un monto a depositar: "))
    # account_balance = account_balance + amount
    account_balance += amount
    print(f"Nuevo balance disponible {account_balance}")
  elif option == 2: # else if -> sino si
    # 2. Retirar Dinero
    print(f'El monto disponible para retiros es de: {account_balance}')
    amount = float(input("Por favor ingrese el monto a retirar: "))

    if amount <= account_balance:
      account_balance -= amount
      print(f"Nuevo balance disponible {account_balance}")
    else: # sino
      print('No se puede retirar mas dinero del disponible!')
  elif option == 3:
    # Hacer un prestamos
    # Como maximo del 30% del saldo disponible
    amount = float(input('Ingrese el monto a solicitar: '))
    max_amount = account_balance * (30/100)

    if amount <= max_amount:
      time = 12 # months
      interest_rate = 16 / 100
      interest = amount * ((1 + interest_rate/time) ** time) - amount
      monthly_payments = (amount + interest) / time
      print(f'El prestamo debera pagarse mensualmente con un cuota de {monthly_payments}')

    else:
      print('No tienes suficiente dinero para fondear el prestamo!')
  elif option == 4:
    print('ESTA SECCIÓN ES SOLO PARA ADMINISTRADORES ... ')
    sum_balances = 0

    for index in range(len(accounts_balance)):
      sum_balances += accounts_balance[index]
      print(f'Cuenta: {index} - Balance: {accounts_balance[index]}')

    print(f'El total de los balances disponibles en el banco es: {sum_balances}')
  else:
    print('Haz ingresado un opción invalida!')

  if idx != SECRET_CODE:
    accounts_balance[idx] = account_balance

  ans = input('Desea continuar? (y/n): ').lower()
