#Check if an Array is Sorted
def is_sorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

if __name__ == "__main__":
    arr1 = [1, 2, 6, 7, 8]
    n = len(arr1)
    result = is_sorted(arr1, n)
    print("The answer is", result)

if __name__ == "__main__":
    arr2 = [8,9,9,7]
    n = len(arr2)
    result = is_sorted(arr2, n)
    print("The answer is", result)