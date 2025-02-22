# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
#     x,  x,x,    x,x     x,       x

num = int(input('Por favor ingrese un número: '))

while num > 0:
  if num % 3 == 0 and num % 5 == 0:
    print('fizzbuzz')
  elif num % 3 == 0:
    print('fizz')
  elif num % 5 == 0:
    print('buzz')
  else:
    print(num)
  num -= 1
