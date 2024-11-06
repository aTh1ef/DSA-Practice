class Solution:
    def spiralOrder(self, matrix):
        # Define ans array to store the result.
        ans = []

        # Get the number of rows and columns
        n = len(matrix)
        m = len(matrix[0])

        # Initialize the pointers required for traversal.
        top, left = 0, 0
        bottom, right = n - 1, m - 1

        # Loop until all elements are traversed.
        while top <= bottom and left <= right:
            # Traverse from left to right.
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom.
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Traverse from right to left.
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Traverse from bottom to top.
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
