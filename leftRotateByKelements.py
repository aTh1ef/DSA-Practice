# Rotate array by K elements
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(arr, k):
    n = len(arr)
    k = k % n

    # Reverse the first k elements
    reverse(arr, 0, k - 1)

    # Reverse the next elements
    reverse(arr, k, n - 1)

    # Reverse the entire array
    reverse(arr, 0, n - 1)

    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 2
    result = rotate(arr, k)
    print(f"After rotating the elements to left by k elements", result)
