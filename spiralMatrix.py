#neetcode 44
class Solution:
    def spiralOrder(self, matrix):
        res = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)

        while l < r and t < b:
            # move from left to right
            for i in range(l, r):
                res.append(matrix[l][i])
            t += 1
            # move from top to bottom
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and t < b):
                break

            # move right to left
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1

            # move bottom to top
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res
