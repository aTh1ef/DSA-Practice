# Write a Python function that calculates and prints the total cost of products based on their prices and quantities.
def calculate_total_with_quantity(prices, quantity):
    total = 0
    for i in range (len(prices)):
        item_total = prices[i] * quantity[i]
        print("Product:", prices[i], "Quantity:", quantity[i], "Item Total:", item_total)
        total += item_total
    print("Total:", total)

if __name__ == "__main__":
    prices1 = [100,200,50,300]
    quantity1 = [2,1,5,1]
    calculate_total_with_quantity(prices1, quantity1)
