#Write a function to rotate a given n×n matrix by 90 degrees clockwise in-place without using extra space.

def rotateMatrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotateMatrix(matrix)  # Function modifies matrix in-place

    # Print rotated matrix
    print("Matrix after rotation:")
    for row in matrix:
        print(row)