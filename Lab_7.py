with open("F1.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
matrix = [[int(num) for num in line.split(',')] for line in lines]
sorted_matrix = sorted(matrix, key=lambda row: sum(1 for num in row if num > 0))
for row in sorted_matrix:
    print(row)
with open("FR.txt", "w") as f:
    for row in sorted_matrix:
        f.write(','.join(map(str, row)) + '\n')
