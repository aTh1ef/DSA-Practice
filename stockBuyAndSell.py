def profit(arr):
    minBuyingPrice = float('inf')
    maxProfit = 0

    for i in range(len(arr)):
        minBuyingPrice = min(minBuyingPrice, arr[i])
        maxProfit = max(maxProfit, arr[i] - minBuyingPrice)

    return maxProfit

if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    result = profit(arr)
    print("The max profit is", result)
