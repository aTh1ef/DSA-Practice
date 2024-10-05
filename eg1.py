#Write a Python program that takes a list of product prices, calculates the total cost of all products, and prints the price of each product along with the total.
def calculate_total(prices):
    total = sum(prices)
    for i in range(len(prices)):
        print("Product", prices[i])
    print("Total", total)

if __name__ == "__main__":
    product_prices = [100,200,7,60]
    calculate_total(product_prices)