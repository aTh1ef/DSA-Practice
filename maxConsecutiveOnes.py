# Count Maximum Consecutive One's in the array
def maxConsecutive(arr,n):
    cnt = maxi = 0
    for i in range(0,n):
        if arr[i] == 1:
            cnt += 1
            maxi = max(maxi, cnt)
        else:
            cnt = 0
    return maxi

if __name__ == "__main__":
    arr=[1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1]
    n=len(arr)
    result = maxConsecutive(arr,n)
    print("The Count of Maximum Consecutive One's in the array is", result)