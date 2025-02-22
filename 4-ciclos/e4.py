total: int = 0
num = 0

while num >= 0:
  num = int(input('Por favor ingrese un número a sumar: ')) # 1
  if num < 0:
    break
  total += num # 1
  # num = int(input('Por favor ingrese un número a sumar: ')) # -1

print(f'El total de la suma es: {total}')



