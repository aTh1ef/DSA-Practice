#Write a function to rotate a given n×n matrix by 90 degrees clockwise in-place without using extra space.
#neetcode 43
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

#alternate solution

# solution with manual reverse function
# class Solution:
#     def rotate(self, matrix):
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         for i in range(n):
#             self.manual_reverse(matrix[i])

#     def manual_reverse(self, lst):
#         left = 0
#         right = len(lst) - 1
#         while left < right:
#             lst[left], lst[right] = lst[right], lst[left]
#             left += 1
#             right -= 1
