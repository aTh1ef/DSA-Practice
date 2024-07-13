# Move all Zeros to the end of the array
def move_arrays(arr,n):
    j=0
    for i in range(n):
        if arr[i] != 0:
         arr[i] ,arr[j] =arr[j], arr[i]
         j +=1

    return arr

if __name__=="__main__":
    arr = [1,0,0,0,22,5,0,8,9,10]
    n = len(arr)
    result=move_arrays(arr,n)
    print("The new array is", result)