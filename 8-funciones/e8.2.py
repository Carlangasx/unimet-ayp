import typing

def count_smaller(numbers:list) -> list:
	counter_list:list = []
	

	for i in numbers:
		contador: int = 0
		for j in numbers:
			if j < i:
				contador += 1
		counter_list.append(contador)
	return counter_list

def main():
	in_ = input('Ingrese una lista de numeros: ')
	nums:list = []
	#limpiar la lista de valores que no sean numeros
	for _ in in_:
		if _.isdigit():
			nums.append(_)
	print(count_smaller(nums))
	    

main()
