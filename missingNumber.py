# Find the missing number in an array
def missingNumber(arr,n):
    sumOfNnumbers = (n*(n+1))//2
    sumOfGivenArray = sum(arr)

    missingNo= sumOfNnumbers - sumOfGivenArray
    return missingNo

if __name__ == "__main__":
    arr = [1,2,4,5]
    n=5
    result = missingNumber(arr,n)
    print("The missing number is", result)



