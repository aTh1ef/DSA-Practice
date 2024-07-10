#Find Second Largest Element in an Array
def secondLargest(arr, n):
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
    arr1 = [2, 7, 7, 9, 3]
    n = len(arr1)
    slargenumber = secondLargest(arr1, n)
    print("The second largest number in the array is", slargenumber)


#Find Second Smallest Element in an Array

def secondSmallest(arr,n):
    if n<2:
        return -1
    smallest = float('inf')
    secondsmall = float('inf')
    for i in range(0,n):
        if arr[i] < smallest:
            secondsmall = smallest
            smallest = arr[i]
        elif arr[i] < secondsmall and arr[i] != smallest:
            secondsmall = arr[i]

    return secondsmall

if __name__ == "__main__":
    arr2 = [2, 7, 7, 9, 3]
    n = len(arr2)
    secondsmallest = secondSmallest(arr2, n)
    print("The second smallest number in the array is", secondsmallest)
