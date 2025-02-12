# Operaciones básicas de manejo de cuenta:
#  - Ver el balance de la cuenta
#  - Retirar dinero
#  - Depositar

balance: float = 0.0

option = input('''
  BIENVENIDO AL BANCO UNIMET
  -------------------------
  1. Depositar
  2. Retirar
''')

if option == '1':
  # Monto para depositar
  amount: float = float(input('Por favor ingrese el valor a depositar: '))
  balance += amount # balance = balance + amount
elif option == '2':
  # Monto para retirar
  amount: float = float(input('Por favor ingrese un monto para retirar: '))
  if amount <= balance:
    balance -= amount
    print(f'El balance disponible es {balance}')
  else:
    print(f'El monto {amount} es mayor que el balance disponible: {balance}')
else:
  print('Haz ingresado un dato invalido')
