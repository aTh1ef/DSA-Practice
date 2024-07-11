#Remove Duplicates in-place from Sorted Array

from typing import List
def removeDuplicate(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j] :
            i +=1
            arr[i] = arr[j]
    return i+1

if __name__ == "__main__":
    arr=[1,1,2,2,2,3,3]
    k= removeDuplicate(arr)
    print("The array after removing the duplicates is ")
    print(arr[:k])

