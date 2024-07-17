# Find Longest Subarray with given Sum K(Positives)
def getLongestSubarray(arr,k):
    n = len(arr)
    left = 0
    sum = 0
    maxLen = 0

    for right in range(n):
        sum += arr[right]

        while sum > k and left <= right:
            sum -= arr[left]
            left += 1

        if sum == k:
            maxLen = max(maxLen, right - left+1)
    return maxLen

if __name__ == "__main__":
    arr = [2,3,5,1,9]
    k = 10
    result = getLongestSubarray(arr,k)
    print("The longest subarray in the given array is ", result)