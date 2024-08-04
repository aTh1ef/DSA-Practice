# Find the number that appears once
def findOnce(arr,n):
    xorr = 0
    for i in range(0,n):
        xorr ^= arr[i]
    return xorr

if __name__ == "__main__":
    arr=[2,2,1,3,4,3,1,4,10]
    n=len(arr)
    result=findOnce(arr,n)
    print("The number that appear once in the array is", result)