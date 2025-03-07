#neetcode 12
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


# Let's break down this code in a very simple way—imagine you're looking at a day-by-day stock price list and you want to know the best profit you could have made by buying low and selling high. I'll show you every line and explain what it does in simple terms, plus give a visual example.

# ---

# ## The Code

# ```python
# class Solution(object):
#     def maxProfit(self, arr):
#
#         maxPro = 0
#         minPrice = float('inf')
#
#         # Iterate through the list of prices
#         for i in range(len(arr)):
#             # Update the minimum price encountered so far
#             minPrice = min(minPrice, arr[i])
#             # Calculate the maximum profit possible at the current price
#             maxPro = max(maxPro, arr[i] - minPrice)
#
#         return maxPro
# ```

# ---

# ## Line-by-Line Explanation in Plain Language

# 1. **`class Solution(object):`**
#    - **What it does:** This line creates a **blueprint** called `Solution`.
#    - **In simple terms:** Think of it as defining a new "box" where your function lives. Platforms like LeetCode often expect you to wrap your solution in a class.

# 2. **`def maxProfit(self, arr):`**
#    - **What it does:** This defines a **function** named `maxProfit` inside the class. It takes one parameter: `arr`, which is a list of stock prices.
#    - **In simple terms:** This is the main function that will look at your list of prices and figure out the best profit you can make.

# 3. **`maxPro = 0`**
#    - **What it does:** This line sets up a variable `maxPro` (short for "maximum profit") and starts it at **0**.
#    - **In simple terms:** Before checking any prices, we assume you haven't made any profit yet.

# 4. **`minPrice = float('inf')`**
#    - **What it does:** This sets up a variable `minPrice` and assigns it an **infinite** value.
#    - **In simple terms:** We start with a very high "minimum" price so that any real price you see will be lower. It's like starting with the worst-case scenario and then improving it.

# 5. **`# Iterate through the list of prices`**
#    - **What it does:** This is a **comment** to tell you what the next block of code will do.
#    - **In simple terms:** We're going to look at each price in the list one by one.

# 6. **`for i in range(len(arr)):`**
#    - **What it does:** This starts a **loop** that goes through every index (`i`) of the list `arr`.
#    - **In simple terms:** It's like checking every day's stock price one at a time.

# 7. **`# Update the minimum price encountered so far`**
#    - **What it does:** This comment explains that the next line is about keeping track of the cheapest price we've seen.
#    - **In simple terms:** We want to remember the lowest price we've come across up to the current day.

# 8. **`minPrice = min(minPrice, arr[i])`**
#    - **What it does:** This compares the current `minPrice` with the current price `arr[i]` and keeps the smaller one.
#    - **In simple terms:** If today's price is lower than any price we've seen before, we update our "cheapest price" to today's price.

# 9. **`# Calculate the maximum profit possible at the current price`**
#    - **What it does:** This comment tells you the next step is to see how much profit you could make if you sold on this day.
#    - **In simple terms:** Now that we know the cheapest price so far, we figure out if selling today gives a better profit than before.

# 10. **`maxPro = max(maxPro, arr[i] - minPrice)`**
#     - **What it does:** This calculates the profit for the current day (`arr[i] - minPrice`) and updates `maxPro` if this profit is greater than what we've seen.
#     - **In simple terms:** It's like asking, "If I bought at the cheapest price I've seen and sold today, would I make more money than before?" If yes, update your best profit.

# 11. **`return maxPro`**
#     - **What it does:** After checking all the prices, this returns the highest profit found.
#     - **In simple terms:** When you're done looking at every day's price, give me the best profit possible.

# ---

# ## Visual Example

# Imagine you have these stock prices for 6 days: `[7, 1, 5, 3, 6, 4]`.

# - **Start:**
#   - `minPrice` is **infinity**, `maxPro` is **0**.
#
# - **Day 1 (Price = 7):**
#   - Update `minPrice = min(inf, 7)` → now `minPrice = 7`.
#   - Profit if selling today: `7 - 7 = 0`.
#   - `maxPro` remains `max(0, 0) = 0`.

# - **Day 2 (Price = 1):**
#   - Update `minPrice = min(7, 1)` → now `minPrice = 1` (a new, lower price!).
#   - Profit: `1 - 1 = 0`.
#   - `maxPro` remains `max(0, 0) = 0`.

# - **Day 3 (Price = 5):**
#   - `minPrice` is still `1`.
#   - Profit: `5 - 1 = 4`.
#   - Update `maxPro = max(0, 4)` → now `maxPro = 4`.

# - **Day 4 (Price = 3):**
#   - `minPrice` is still `1`.
#   - Profit: `3 - 1 = 2`.
#   - `maxPro` stays `max(4, 2) = 4` (since 4 is higher).

# - **Day 5 (Price = 6):**
#   - `minPrice` is still `1`.
#   - Profit: `6 - 1 = 5`.
#   - Update `maxPro = max(4, 5)` → now `maxPro = 5`.

# - **Day 6 (Price = 4):**
#   - `minPrice` remains `1`.
#   - Profit: `4 - 1 = 3`.
#   - `maxPro` stays `max(5, 3) = 5`.

# **Result:** The best profit is **5** (buy at 1 on Day 2 and sell at 6 on Day 5).

# ---

# ## Summing It Up

# - **Keep track of the cheapest price:**
#   Every time you see a new price, check if it's lower than your current lowest (using `minPrice`).

# - **Calculate potential profit:**
#   At each price, see what the profit would be if you bought at the cheapest price and sold now.

# - **Remember the best profit:**
#   Always update your best profit (`maxPro`) if the new profit is higher.

# - **Return the best profit found:**
#   After checking all prices, you get the maximum profit possible.

# By visualizing the process day by day, you can see that the code is just a smart way of keeping track of the best time to buy (lowest price so far) and the best time to sell (highest profit from that lowest price). This method makes sure you only pass through the list once, which makes it very efficient.

# I hope this makes things super clear!

