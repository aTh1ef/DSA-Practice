#Your goal is to find a group of numbers next to each other (a subarray) that adds up to the biggest total. Then, you need to return that total.
def maxSubArray (arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    arr =  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maxSubArray(arr)
    print("the sum of max sub array is", result )