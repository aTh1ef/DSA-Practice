def secondLargestrev(arr):
    n = len(arr)
    largest = float('-inf')
    slargest = float('-inf')

    for i in range(0,n):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]

        elif arr[i] > slargest and arr[i] != largest:
            slargest = arr[i]

    return slargest

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    second = secondLargestrev(arr)
    print("The second largest element in the array is:", second)