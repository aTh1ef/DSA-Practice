#Remove Duplicates in-place from Sorted Array
def removeDuplicate(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j] :
            i += 1
            arr[i] = arr[j]
    return i+1

if __name__ == "__main__":
    arr=[1,1,2,2,2,3,3]
    result = removeDuplicate(arr)
    print("The array after removing the duplicates is ", arr[:result])


    if __name__ == "__main__":
        arr = [1, 1, 7, 7, 88, 88]
        result = removeDuplicate(arr)
        print("The array after removing the duplicates is ", arr[:result])


