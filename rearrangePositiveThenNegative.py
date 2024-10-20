# Rearrange the numbers in the list so that positive and negative numbers alternate, starting with a positive number.
def rearrange(arr):
    positive = []
    negative = []

    for i in range(len(arr)):
        if arr[i] > 0:
            positive.append(arr[i])
        else:
            negative.append(arr[i])

    result = []

    for i in range(len(positive)):
        result.append(positive[i])
        result.append(negative[i])

    return result

if __name__ == "__main__":
    arr = [-1, -2, 4, 9, 8, -5]
    answer = rearrange(arr)
    print("The rearranged array is as follows:", answer)