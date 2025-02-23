#Find the majority element in an array using the Boyer-Moore Voting Algorithm

def majorityElement(arr):
    n = len(arr)
    cnt = 0
    el = 0
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]

        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    cnt1 = 0
    for i in range(n):
        if arr[i] == el :
            cnt1 += 1

    if cnt1 > n/2:
        return el
    return -1

if __name__ == "__main__":
    arr = [2,3,3,4,5,6,7,8,3,3,3,3,3,3]
    result = majorityElement(arr)
    print("The majority element is", result)

