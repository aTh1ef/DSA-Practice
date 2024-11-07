from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):

        # Dictionary to store counts of each running total we’ve seen
        running_total_count = defaultdict(int)
        running_total = 0  # The cumulative sum as we go through the list
        count = 0  # Total number of subarrays that sum up to k

        # Initialize with 0 to handle cases where subarrays start from index 0
        running_total_count[0] = 1

        # Loop through each number in nums
        for num in nums:
            running_total += num  # Update the cumulative running total

            # Check if (running_total - k) exists in the dictionary
            count += running_total_count[running_total - k]

            # Update the dictionary with the current running total
            running_total_count[running_total] += 1

        return count
