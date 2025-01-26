import typing
vectors = [
    (1, 7, 2),
    (2, 3, 5)
]

# Your code
riqueza: list = []

for i in range(len(vectors)):
    total : int = 0
    for j in range(len(vectors[i])):
        total += vectors[i][j]
    riqueza.append(total)
riqueza.sort()

print(f'La riqueza mas grande es {riqueza[-1]}')