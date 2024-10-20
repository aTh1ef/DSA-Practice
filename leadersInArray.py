#Find all the leaders in an array, where a leader is an element that is greater than all the elements to its right.
def leaders(arr):
    ans = []
    n = len(arr)

    maxElement = arr[-1]
    ans.append(maxElement)

    for i in range(n-2, -1, -1):
        if arr[i] > maxElement:
            ans.append(arr[i])
            maxElement = arr[i]

    return ans[::-1]

if __name__ == "__main__":
    arr = [10, 22, 12, 3, 0, 6]
    result = leaders(arr)
    print("The leaders of the array are:", result)
