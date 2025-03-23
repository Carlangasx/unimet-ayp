
def is_prime(num):
  aux = 2
  while aux < num:
    if num % aux == 0:
      return False
    aux += 1
  return True

def is_defficent(num): 
  aux = 1
  acc = 0
  while aux < num:
    if num % aux == 0:
      acc += aux
    aux += 1
  return acc < num

def factorial(num):
  if num == 0 or num == 1:
    return 1
  return num * factorial(num - 1)


def get_factorial_set(num):
  result = []
  for n in range(1, num + 1):
    result.append(factorial(n))
  return result

