#neetcode 36

class Solution(object):
    def maxSubArray(self, nums):
        curSum = 0
        maxSum = nums[0]

        # looping through every number in thr array
        for i in range(len(nums)):
            n = nums[i]
            # if the current sum is less than zero we reset it to 0
            if curSum < 0:
                curSum = 0
                # we increment the curSum as we loop through the array
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum


# This function implements Kadane's algorithm to find the maximum subarray sum
# A subarray is a contiguous part of an array (i.e., a slice of consecutive elements)
# The goal is to find the subarray with the largest sum

# Let's break down how this works:

# Initialize two variables:
# - curSum: keeps track of the current running sum of elements
# - maxSum: stores the maximum sum found so far, starting with the first element

# We start by assuming the first element is our maximum sum
# This handles the case where all numbers are negative (the answer would be the largest negative number)

# As we iterate through the array:
# 1. If curSum becomes negative, we reset it to 0
#    Why? Because carrying a negative sum would only decrease future sums
#    It's better to start fresh from the current element
# 
# 2. We add the current element to curSum
#
# 3. We update maxSum if curSum is larger
#    This captures the maximum subarray sum we've seen so far

# Example walkthrough with nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]:
# 
# Initialize: curSum = 0, maxSum = -2
#
# i=0: n = -2, curSum = 0 + (-2) = -2, maxSum = max(-2, -2) = -2
# i=1: n = 1, curSum < 0 so reset curSum = 0, then curSum = 0 + 1 = 1, maxSum = max(-2, 1) = 1
# i=2: n = -3, curSum = 1 + (-3) = -2, maxSum = max(1, -2) = 1
# i=3: n = 4, curSum < 0 so reset curSum = 0, then curSum = 0 + 4 = 4, maxSum = max(1, 4) = 4
# i=4: n = -1, curSum = 4 + (-1) = 3, maxSum = max(4, 3) = 4
# i=5: n = 2, curSum = 3 + 2 = 5, maxSum = max(4, 5) = 5
# i=6: n = 1, curSum = 5 + 1 = 6, maxSum = max(5, 6) = 6
# i=7: n = -5, curSum = 6 + (-5) = 1, maxSum = max(6, 1) = 6
# i=8: n = 4, curSum = 1 + 4 = 5, maxSum = max(6, 5) = 6
#
# Final result: 6 (the subarray is [4, -1, 2, 1])

# Time Complexity: O(n) - we only need to iterate through the array once
# Space Complexity: O(1) - we only use two variables regardless of input size