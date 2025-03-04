#Given an array of integers and a target sum, how can you find the indices of the two numbers that add up to the target?
def twoSums(arr, target):
    arr_map = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in arr_map:
            return [arr_map[complement], i]
        arr_map[arr[i]] = i

if __name__ == "__main__":
    arr = [10,20,30,5]
    target = 15
    result = twoSums(arr, target)
    print(result)
