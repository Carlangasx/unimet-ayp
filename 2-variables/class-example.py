# Operaciones básicas de manejo de cuenta:
#  - Ver el balance de la cuenta
#  - Retirar dinero
#  - Depositar

balance: float = 0.0

# Monto para depositar
amount: float = float(input('Por favor ingrese el valor a depositar: '))
balance += amount # balance = balance + amount

# Monto para retirar
amount: float = float(input('Por favor ingrese un monto para retirar: '))
balance -= amount


print(balance)
