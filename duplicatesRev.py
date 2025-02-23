def leader(arr):
    n = len(arr)
    ans = []
    max_element = arr[-1]
    ans.append(max_element)

    for i in range(n-2,-1,-1):
        if arr[i] > max_element:
            ans.append(arr[i])
            max_element = arr[i]

    return ans

if __name__ == "__main__":
    arr = [10, 22, 12, 3, 0, 6]
    ans = leader(arr)
    print("the answer is:", ans)
