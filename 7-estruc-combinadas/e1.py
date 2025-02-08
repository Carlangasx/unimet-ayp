import typing

new_list: list = []
accounts = [
    [1, 5, 10, 12],
    [7, 3, 10, 12],
    [3, 5, 10, 12]
]

for account in accounts:
    for value in account:
        new_list.append(value)

new_list.sort()
print(f'{new_list}')

