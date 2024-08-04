#Find Largest Element in an array
def find_largest(arr, n):
    max = arr[0]
    for i in range(n):
        if max < arr[i]:
            max = arr[i]
    return max

if __name__ == "__main__":
    arr1 = [1, 9, 8, 4, 2]
    n = 5
    max_element = find_largest(arr1, n)
    print("The largest number in the array is", max_element)

if __name__ == "__main__":
    arr1 = [200, 240, 1000, 17, 9000]
    n = 5
    max_element = find_largest(arr1, n)
    print("The largest number in the array is", max_element)
