# divisibles = 0

# numero = int(input('Por favor ingrese un numero: '))

# divisor = 1

# while divisor <= numero:
#   if numero % divisor == 0:
#     divisibles += 1
#   divisor += 1

# if divisibles == 2:
#   print(f'El numero {numero} es primo')
# else:
#   print(f'El numero {numero} NO es primo')

num = int(input('Por favor ingrese un numero: '))

is_prime = True

div = 2

while div < num:
  if num % div == 0:
    is_prime = False
    break
  div += 1

if is_prime:
  print(f'El numero {num} es primo')
else:
  print(f'El numero {num} NO es primo')
