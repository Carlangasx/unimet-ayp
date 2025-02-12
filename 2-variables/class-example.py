# Modelar o hacer el sistema de un banco

account_balance: float = 0.0

# 1. Depositar
amount = float(input("Por favor ingrese un monto a depositar: "))

# account_balance = account_balance + amount
account_balance += amount


print(f"Nuevo balance disponible {account_balance}")
# print("Nuevo balance disponible: {}".format(account_balance))

# 2. Retirar Dinero
amount = float(input("Por favor ingrese el monto a retirar: "))

# account_balance = account_balance - amount
account_balance -= amount

overdraft = account_balance < 0 # < > <= >= ==  != <=

print(f"Nuevo balance disponible {account_balance}")
print(f"La cuenta esta sobregriada?: {overdraft}")

# 3. Generar intereses

# I = VF - VA
# VF = VA * (1 + i)^n

time = 6 # meses

interest_rate = 16 / 100

interest = account_balance * ((1 + interest_rate) ** time) - account_balance

account_balance += interest

print(f"Mis intereses generados son: {interest}")
print(f"Nuevo balance disponible {account_balance}")

