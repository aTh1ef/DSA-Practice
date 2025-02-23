# You are given an array of ‘N’ integers.
# You need to find the length of the longest sequence which contains the consecutive elements.

def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in nums:
        if num - 1 not in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2, 2, 5]
    answer = longestConsecutive(nums)
    print("The longest consecutive sequence in the array is", answer)