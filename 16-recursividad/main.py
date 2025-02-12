
def nr_factorial(n):
  result = 1
  for aux in range(2, n+1):
    result *= aux
  return result


def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n-1)


# f(0) = 0
# f(1) = 1
# f(2) = f(0) + f(1) = 1
# f(3) = f(1) + f(2) = 2
# f(4) = f(2) + f(3) = 3
# f(5) = f(3) + f(4) = 5

cache = {
  0: 0,
  1: 1
}

def fibonacci(n):
  if n == 0 or n == 1:
    return n
  if cache.get(n) != None:
    return cache[n]
  cache[n] = fibonacci(n-2) + fibonacci(n-1)
  return cache[n]
  # return fibonacci(n-2) + fibonacci(n-1)


def main():
  num = 500
  # result_nr = nr_factorial(num)
  # print(f'Resultado no usando recursividad:')
  # result_r = factorial(num)
  # print(f'Resultado usando recursividad:')
  print(fibonacci(100))
main()
