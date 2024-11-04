#Given an m x n integer matrix, if any element in the matrix is 0, the entire row and column containing that element should be set to 0. This needs to be done in place without using additional memory for marking.
def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col0 = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0


    for i in range(1,n):
        for j in range(1,m):
            if matrix [i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0


    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0


if __name__ == "__main__":
    matrix =  [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix)
    print("the result is")
    for row in matrix:
        print(row)