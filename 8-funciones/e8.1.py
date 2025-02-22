import typing

def main():
  while True:
    contador: int = 0
    number = int(input("Ingrese un número: "))
    pairs:set = ()
    
    pairs.add(numbers[-1]+1)
    print(f'{numbers}')

    for i in range(number):
      pairs.add(i)
      i += 1
      if pairs[i] % i == 0:
        contador += 1
    if contador > 2:
      pairs[1]
    else:
      print('primo')  

main()