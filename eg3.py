#Write a Python function that takes a list of product prices and a threshold value. The function should filter out and display the prices that are greater than the threshold.

def calculate(prices, threshold):
    above_threshold = []
    for i in range(len(prices)):
        if prices[i] > threshold:
            above_threshold.append(prices[i])
    print("Expensive products:" , above_threshold)

if __name__ == "__main__":
    prices = [100,200,50,300]
    threshold = 150
    calculate(prices,threshold)
