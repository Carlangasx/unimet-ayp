import typing

def main():
    #solicitar input
    array: list[int] = input("Enter the array: ")
   #convertir el input en una lista de enteros
    array = [int(x) for x in array if x.isdigit()]

    #encontrar los picos
    def picos(array_numerica: list[int]) -> list[int]:
        picos:list[int] = [] 
        for i in range(1, len(array_numerica)-1):
            if array_numerica[i] > array_numerica[i-1] and array_numerica[i] > array_numerica[i+1]:
                picos.append(array_numerica[i])
            else: 
                continue
        return picos
    print(picos(array))
    print(type(array), array)

main()