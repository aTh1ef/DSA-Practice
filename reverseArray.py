def reverseArray(nums):
    n = len(nums)
    left, right = 0, n-1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return(nums)

print(reverseArray([1,2,3,4,5,9,10,11]))