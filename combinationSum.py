#neetcode34
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        # first we create a helper function
        def dfs(i, cur, total):
            # condition to check if we have met the target
            if total == target:
                res.append(list(cur))
                return
            # condition to check if the index has gone out of bounds or the total is exceeding the target
            if i >= len(candidates) or total > target:
                return

                # pick the number at index i
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # backtrack and move to the next number
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

# ### Overall Goal of the Code

# **What it does:**
# The code finds all unique combinations of numbers from the list `nums` that add up exactly to the given `target`. It does this using a depth-first search (DFS) approach with backtracking. Think of it as exploring a tree where each branch is a choice of adding a number or not.

# ---

# ### Code Walkthrough with Visualizations

# #### **Step 1: Function Definition and Setup**

# ```python
# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
# ```

# **Explanation:**
# - **What happens:**
#   - A class `Solution` is defined with a method `combinationSum`.
#   - Inside this method, an empty list `res` is created to store all valid combinations.
# - **Layman Explanation:**
#   - Imagine you have an empty basket (`res`) where you will put all the sets of numbers that add up to the target.

# **Visualization:**

# ```
# +--------------------------------------+
# | Function combinationSum(nums, target)|
# |                                      |
# |   res = []   <-- empty basket       |
# +--------------------------------------+
# ```

# ---

# #### **Step 2: Defining the Recursive Function**

# ```python
#         def dfs(i, cur, total):
# ```

# **Explanation:**
# - **What happens:**
#   - A helper function `dfs` (depth-first search) is defined inside `combinationSum`.
#   - It takes three parameters:
#     - `i`: The current index in `nums`.
#     - `cur`: The current combination being built.
#     - `total`: The sum of numbers in the current combination.
# - **Layman Explanation:**
#   - Think of `dfs` as a worker that picks numbers from your list. It keeps track of which number you're at (`i`), the current list of picked numbers (`cur`), and how much they add up to (`total`).

# **Visualization:**

# ```
# +-------------------------------+
# |  dfs(i, cur, total)           |
# |                               |
# |  i: current index             |
# |  cur: current combination     |
# |  total: current sum           |
# +-------------------------------+
# ```

# ---

# #### **Step 3: Base Case – When Total Matches the Target**

# ```python
#             if total == target:
#                 res.append(cur.copy())
#                 return
# ```

# **Explanation:**
# - **What happens:**
#   - The code checks if the current sum (`total`) equals the target.
#   - If yes, it copies the current combination `cur` into the results list `res` and stops further exploration along that branch.
# - **Layman Explanation:**
#   - When the numbers you've picked add up exactly to what you want, you take a snapshot (copy the list) and add it to your basket (`res`). Then, you stop going deeper along that branch.

# **Visualization:**

# ```
#          [ Branch: cur = [a, b, c] ]
#                  |
#        total == target? --> Yes
#                  |
#        Add [a, b, c] to res  and return.
# ```

# ---

# #### **Step 4: Base Case – When You've Gone Too Far or Out of Bounds**

# ```python
#             if i >= len(nums) or total > target:
#                 return
# ```

# **Explanation:**
# - **What happens:**
#   - If the index `i` is out of range (meaning you've looked at all numbers) or if the current sum `total` exceeds the target, the function returns without doing anything.
# - **Layman Explanation:**
#   - If you run out of numbers to check or your current total is too high, you stop exploring that path. It's like realizing you're going down the wrong street and turning back.

# **Visualization:**

# ```
#    [ Branch: cur = [a, b, c] ]
#          |
# total > target? or i out of range?
#          |
#        Return (backtrack)
# ```

# ---

# #### **Step 5: Decision – Choose the Current Number (Include it)**

# ```python
#             cur.append(nums[i])
#             dfs(i, cur, total + nums[i])
# ```

# **Explanation:**
# - **What happens:**
#   - The number at index `i` is added to the current combination (`cur`).
#   - Then, `dfs` is called again with:
#     - The same index `i` (because you can use the same number more than once),
#     - The updated combination `cur`, and
#     - The updated sum (`total + nums[i]`).
# - **Layman Explanation:**
#   - You decide to take the current number. Imagine you add a new ingredient to your recipe and check if you're getting closer to the perfect taste (target sum).
#   - You don't move to the next number yet because you can use the same ingredient repeatedly.

# **Visualization:**

# ```
#          Before: cur = [a, b]
#          Pick nums[i] = c
#          After:  cur = [a, b, c]
#          New total = total + c
#          Continue DFS from same index (i)
# ```

# ---

# #### **Step 6: Backtracking – Remove the Last Number (Don't Include it)**

# ```python
#             cur.pop()
#             dfs(i + 1, cur, total)
# ```

# **Explanation:**
# - **What happens:**
#   - After exploring the branch where the current number was added, the function removes it (backtracks) to try a different path.
#   - Then, it calls `dfs` with the next index (`i + 1`), leaving `cur` and `total` unchanged.
# - **Layman Explanation:**
#   - Once you've tried a particular ingredient, you remove it to see what happens if you don't include it. It's like saying, "Okay, what if I don't use this ingredient?" and then moving to the next option.

# **Visualization:**

# ```
#          [ Branch where you added c ]
#          ----------------------------
#          Backtrack: remove c
#          Now: cur = [a, b]
#          Then: move to next index: i + 1
# ```

# ---

# #### **Step 7: Starting the DFS and Returning the Result**

# ```python
#         dfs(0, [], 0)
#         return res
# ```

# **Explanation:**
# - **What happens:**
#   - The DFS process starts at index `0` with an empty combination (`cur = []`) and a sum of `0`.
#   - Once all possibilities are explored, the function returns the `res` list containing all valid combinations.
# - **Layman Explanation:**
#   - Think of this as starting your search from the beginning of your list with nothing in your basket and an empty total. When you're done exploring all branches, you hand back your basket filled with all the winning recipes.

# **Visualization:**

# ```
#         Start DFS:
#         i = 0, cur = [], total = 0
#                |
#        Explore all possible paths
#                |
#         End DFS -> return res (basket filled with recipes)
# ```

# ---

# ### Final Visualization Summary

# Imagine the process as a tree where every node represents a decision (to include a number or not):

# ```
#           (Start: i=0, cur=[], total=0)
#                      |
#        ---------------------------------
#        |                               |
# Include nums[0] (say 2)        Skip nums[0]
#        |                               |
# (cur = [2], total = 2)         (cur = [], total = 0)
#        |                               |
#     Continue DFS                    Continue DFS
#        ...                             ...
# ```

# At each node, the DFS explores two directions:
# 1. **Include the current number:** The branch where you add `nums[i]` and continue with the same index.
# 2. **Skip the current number:** The branch where you backtrack (remove the last number) and move to the next index.

# When the sum matches the target, you add that branch to your basket (`res`). If the sum goes over or you run out of numbers, you stop going further down that branch.

# ---

# ### Final Thoughts

# - **Recursion and Backtracking:**
#   The function uses recursion to explore every possible combination. When a combination doesn't work out (sum too high or no numbers left), it backtracks by removing the last added number and tries another path.

# - **Why It Works:**
#   By considering every possibility (adding or skipping a number), the algorithm ensures that all valid combinations are found.