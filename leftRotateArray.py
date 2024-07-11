def leftRotate(arr, n):
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    for i in range(n):
     return arr

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    n = 5
    result=leftRotate(arr,n)
    print("The new array is", result)


