matrix=[]

for i in range(3):
    row=[]
    for j in range(3):
        row.append(int(input(f"Enter element at {i}th row and {j}th column: ")))

    matrix.append(row)
print("Matrix is: ")
for row in matrix:
    print(row)