# Operaciones básicas de manejo de cuenta:
#  - Ver el balance de la cuenta
#  - Retirar dinero
#  - Depositar

balance: float = 0.0

ans = 'y'

while ans == 'y':

  option = input('''
    BIENVENIDO AL BANCO UNIMET
    -------------------------
    1. Depositar
    2. Retirar
  ''')

  if option == '1':
    # Monto para depositar
    amount: str = input('Por favor ingrese el valor a depositar: ')
    while not amount.isnumeric():
      if '.' in amount:
        break
      amount = input('Por favor ingrese el valor a depositar: ')
    amount: float = float(amount)
    balance += amount # balance = balance + amount
    print(f'El balance disponible es {balance}')

  elif option == '2':
    # Monto para retirar
    amount: str = input('Por favor ingrese el valor a depositar: ')
    while not amount.isnumeric():
      if '.' in amount:
        break
      amount = input('Por favor ingrese el valor a depositar: ')
    amount: float = float(amount)
    if amount <= balance:
      balance -= amount
      print(f'El balance disponible es {balance}')
    else:
      print(f'El monto {amount} es mayor que el balance disponible: {balance}')
  else:
    print('Haz ingresado un dato invalido')

  ans = input('Desea continuar ejecutando el programa (y/n)?: ').lower()

  while ans != 'y' and ans != 'n':
    ans = input('Ingrese un dato valido: Desea continuar ejecutando el programa (y/n)?: ').lower()

