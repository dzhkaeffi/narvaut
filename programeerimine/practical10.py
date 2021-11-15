llist = [5, 2, 1, 4, 3]
for i in range(len(llist)):
    for j in range(i + 1):
        if llist[j] > llist[i]:
            temp = llist[i]
            llist[i] = llist[j]
            llist[j] = temp
print(llist)

arr = [[5, 6, 7],
       [8, 9, 10]]
# row-by-row
for rownum in range(len(arr)):
    print('Row {}:'.format(rownum), end=' ')
    for elem in (arr[rownum]):
        print(elem, end=' ')
    print()
# col-by-col
j = 0
while j <= len(arr):
    print('Col {}:'.format(j), end=' ')
    for i in range(len(arr)):
        print(arr[i][j], end=' ')
    print()
    j += 1

# matrixproduct
matrix1 = [[1, 2],
           [3, 4]]

matrix2 = [[5, 6, 7],
           [8, 9, 10]]

product = [[0, 0, 0],
           [0, 0, 0]]
for mx1 in range(len(matrix1)):
    for mx2 in range(len(matrix2[0])):
        for mx3 in range(len(matrix2)):
            product[mx1][mx2] += matrix1[mx1][mx3] * matrix2[mx3][mx2]
for r in product:
    print(r)


