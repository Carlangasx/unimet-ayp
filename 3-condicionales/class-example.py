# Modelar o hacer el sistema de un banco

account_balance: float = 100000.0

# Hacer un menu

menu = """
1. DEPOSITAR
2. RETIRAR
3. SOLICITAR PRESTAMO -> NOTA: Solo se podra prestar el 30% del saldo disponible
"""

option = int(input(menu))

if option == 1:
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

else:
  print('Haz ingresado un opción invalida!')

