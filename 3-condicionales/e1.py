import typing

candidate: float = float(input('Por favor ingresa un número: '))

msg = f'El número {candidate} es '

if candidate % 2 == 0:
  msg += 'par y es '
else:
  msg += 'impar y es '

if candidate >= 0:
  msg += 'positivo'
else:
  msg += 'negativo'


print(msg)
