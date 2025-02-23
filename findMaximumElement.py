def maximumArray(arr):
    n = len(arr)
    maximum = arr[0]

    for i in range(0,n):
        if maximum < arr[i]:
            maximum = arr[i]

    return maximum

if __name__ =="__main__":
    arr = [1,2,3,4,5,27]
    maximum = maximumArray(arr)
    print("The maximum value of the array is:", maximum)
