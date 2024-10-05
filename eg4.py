#Given an array of integers and a target sum, how can you find the indices of the two numbers that add up to the target?
def twoSums(nums, target):
    nums_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_map:
            return [nums_map[complement], i]
        nums_map[nums[i]] = i

if __name__ == "__main__":
    nums = [10,20,30,5]
    target = 15
    result = twoSums(nums, target)
    print(result)
