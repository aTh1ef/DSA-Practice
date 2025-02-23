def sorted(arr):
    n = len(arr)
    for i in range (1,n):
        if arr[i] < arr[i-1]:
            return False
    return True

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    sortedd = sorted(arr)
    print("is the array sorted true or false", sortedd)
