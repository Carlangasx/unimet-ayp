import typing

new_list: list = []
accounts = [
    [1, 5, 10, 12],
    [7, 3, 10, 12],
    [3, 5, 10, 12]
]

for i in range(len(accounts)):
    for j in range(len(accounts[i])):
        new_list.append(accounts[i][j])

new_list.sort()
print(f'{new_list}')

