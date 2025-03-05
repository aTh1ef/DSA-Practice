# You are given an array of ‘N’ integers.
# You need to find the length of the longest sequence which contains the consecutive elements.
# neetcode #8
class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            n = nums[i]

            if (n - 1) not in numSet:
                length = 0

                while (n + length) in numSet:
                    numSet.remove(n + length)
                    length += 1

                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2, 2, 5]
    sol = Solution()
    answer = sol.longestConsecutive(nums)
    print("The longest consecutive sequence in the array is", answer)

# Below is the **modified code** that uses a `for i in range(len(nums))` loop instead of directly iterating over the list. The functionality remains the same, and I'll provide a detailed, line-by-line explanation (in simple terms) just like before.

# ---

# ## The Code

# ```python
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # 1) Convert the list to a set for fast lookups
#         numSet = set(nums)
#         # 2) Initialize a variable to keep track of the longest sequence length
#         longest = 0

#         # 3) Loop through the indices of the original list
#         for i in range(len(nums)):
#             n = nums[i]  # Get the current number using its index

#             # 4) Check if 'n' is the start of a consecutive sequence
#             if (n - 1) not in numSet:
#                 # 5) If yes, initialize a counter for the sequence length
#                 length = 0
#                 # 6) While the next consecutive number exists, keep counting
#                 while (n + length) in numSet:
#                     length += 1
#                 # 7) Update the longest sequence found if this one is longer
#                 longest = max(longest, length)
#
#         # 8) Return the length of the longest consecutive sequence
#         return longest
# ```

# ---

# ## Line-by-Line Explanation (Layman Terms)

# ### 1. `class Solution:`
# - **What it does:** Defines a container (class) named `Solution`.
# - **Why:** It's a common pattern in coding problems to wrap your function in a class.

# ### 2. `def longestConsecutive(self, nums: List[int]) -> int:`
# - **What it does:** Defines a function called `longestConsecutive` that takes a list of numbers (`nums`) and returns an integer.
# - **Why:** We need to figure out the longest run of consecutive numbers in the list.

# ### 3. `numSet = set(nums)`
# - **What it does:** Converts the list `nums` into a **set** called `numSet`.
# - **Why:** Sets let you quickly check if a number is present (like asking, "Is 5 here?"). This speeds up the process.

# ### 4. `longest = 0`
# - **What it does:** Creates a variable named `longest` and starts it at 0.
# - **Why:** This variable will keep track of the longest sequence we find.

# ### 5. `for i in range(len(nums)):`
# - **What it does:** Loops through every index in the list `nums`.
# - **Why:** Instead of going directly through each number, we're going through the indices (0, 1, 2, …).

# ### 6. `n = nums[i]`
# - **What it does:** Retrieves the current number (`n`) from the list using its index `i`.
# - **Why:** This makes it easier to work with the number while still using the index loop.

# ### 7. `if (n - 1) not in numSet:`
# - **What it does:** Checks if the number just before `n` (i.e., `n - 1`) is **not** in the set.
# - **Why:** If `(n - 1)` isn't there, it means `n` might be the **start** of a consecutive sequence. For example, if `n` is 3 and 2 isn't in the set, then 3 could be where a new sequence begins.

# ### 8. `length = 0`
# - **What it does:** Sets a counter `length` to 0.
# - **Why:** This counter will measure how many consecutive numbers are in the sequence starting from `n`.

# ### 9. `while (n + length) in numSet:`
# - **What it does:** As long as the number `n + length` exists in the set, the loop continues.
# - **Why:** This loop checks for a consecutive sequence. For example, if `n` is 3, it checks for 3, then 4, then 5, and so on.

# ### 10. `length += 1`
# - **What it does:** Increases the counter `length` by 1 each time a consecutive number is found.
# - **Why:** This keeps track of how long the consecutive sequence is.

# ### 11. `longest = max(longest, length)`
# - **What it does:** Compares the current `length` with the previously recorded `longest` and updates `longest` if the new sequence is longer.
# - **Why:** To always remember the longest sequence found so far.

# ### 12. `return longest`
# - **What it does:** Returns the value of `longest` once all numbers have been processed.
# - **Why:** This is the final answer—the length of the longest consecutive sequence.

# ---

# ## Visual Walkthrough Example

# Let's say our input list is:

# ```python
# nums = [100, 4, 200, 1, 3, 2]
# ```

# 1. **Convert list to set:**
#    - `numSet = {1, 2, 3, 4, 100, 200}`
# 2. **Initialize `longest`:**
#    - `longest = 0`

# 3. **Loop over indices:**
#    - **Index 0:** `n = nums[0] = 100`
#      - Check if 99 (`100 - 1`) is in the set. It's not.
#      - Start a sequence:
#        - Is 100 in the set? Yes (length becomes 1).
#        - Is 101 in the set? No.
#      - Update `longest = max(0, 1) = 1`.
#
#    - **Index 1:** `n = nums[1] = 4`
#      - Check if 3 (`4 - 1`) is in the set. Yes (3 is present).
#      - Skip counting because 4 is not the start of a sequence.
#
#    - **Index 2:** `n = nums[2] = 200`
#      - Check if 199 is in the set. It's not.
#      - Start a sequence:
#        - Is 200 in the set? Yes (length becomes 1).
#        - Is 201 in the set? No.
#      - Update `longest = max(1, 1) = 1`.
#
#    - **Index 3:** `n = nums[3] = 1`
#      - Check if 0 is in the set. It's not.
#      - Start a sequence:
#        - 1 is in the set (length becomes 1).
#        - 2 is in the set (length becomes 2).
#        - 3 is in the set (length becomes 3).
#        - 4 is in the set (length becomes 4).
#        - 5 is not in the set.
#      - Update `longest = max(1, 4) = 4`.
#
#    - **Index 4:** `n = nums[4] = 3`
#      - Check if 2 is in the set. It is, so skip.
#
#    - **Index 5:** `n = nums[5] = 2`
#      - Check if 1 is in the set. It is, so skip.

# 4. **Return Result:**
#    - The function returns `4` because the longest consecutive sequence is `1, 2, 3, 4` which has 4 numbers.

# ---

# ## In the Most Basic Terms

# 1. **Make a set:**
#    - Quickly check if a number exists in our list.
#
# 2. **Loop through each index:**
#    - Get the number at each index.
#
# 3. **Check if it's the start:**
#    - See if the number before it is missing (meaning it's the start of a new sequence).
#
# 4. **Count consecutive numbers:**
#    - Use a loop to count how many numbers in a row are in the set.
#
# 5. **Keep the longest:**
#    - Remember the longest sequence you've found.
#
# 6. **Return that longest count:**
#    - That's your answer!

# This modified version does the exact same work as before but uses indices to loop through the list.

# If your code is **hitting the time limit exceeded (TLE)** in LeetCode, there are a few possible reasons why:

# ---

# ### **Possible Causes & Fixes**

# #### ✅ **1. Large Input Size (~10⁵ elements)**
# - Your code runs in **O(N)** time, which should be fine for **most cases**.
# - However, if `nums` is really large (like $$10^5$$ elements), Python's performance with large sets and loops can be **slower than expected**.

# **🔧 Fix:**
# - Try switching to **C++** (which is generally faster for these types of problems).
# - If sticking with Python, use `pypy3` instead of `python3` (PyPy runs loops faster).

# ---

# #### ✅ **2. Duplicate Elements in `nums`**
# - If `nums` has many duplicate elements, your algorithm **still loops through all elements**, even though they **don't contribute to new sequences**.

# **🔧 Fix:**
# - Before processing, **remove duplicates by using `set(nums)` earlier in the function**.

# ---

# #### ✅ **3. Inefficient Set Operations**
# - The key idea of this approach is that we **only start counting** when we find the smallest number in a sequence (`if (n - 1) not in numSet:`).
# - If `nums` is **very large and random**, checking set membership (`if (n - 1) not in numSet:` and `while (n + length) in numSet:`) can **slow things down**.

# **🔧 Fix:**
# Instead of using `while (n + length) in numSet`, try:
# ```python
# while n + length in numSet:
#     numSet.remove(n + length)  # Remove elements as we process them
#     length += 1
# ```
# **Why does this help?**
# - This avoids **checking the same elements multiple times** in large datasets.

# ---

# #### ✅ **4. LeetCode Python-Specific Issues**
# LeetCode uses **strict time limits** for Python.
# Even if an algorithm is **O(N)**, Python's built-in operations (like set lookups) **are slightly slower** than in C++/Java.

# **🔧 Fix:**
# - Try `pypy3` instead of `python3` in LeetCode.
# - Optimize how you check and process elements.

# ---

# ### **Optimized Code (With Fixes)**
# ```python
# class Solution:
#     def longestConsecutive(self, nums):
#         numSet = set(nums)  # Remove duplicates and store in a set
#         longest = 0

#         for n in numSet:  # Iterate through unique numbers only
#             if (n - 1) not in numSet:  # Only start counting at sequence start
#                 length = 1
#                 while (n + length) in numSet:
#                     numSet.remove(n + length)  # Remove elements to prevent duplicate processing
#                     length += 1
#                 longest = max(longest, length)
#
#         return longest
# ```

# ### **Why is this faster?**
# 1. **Iterating through `numSet` instead of `nums`** → Avoids duplicate elements.
# 2. **Removing elements as we process them** → Prevents redundant checks.
# 3. **No unnecessary operations** → Each number is processed **once and only once**.

# ---

# ### **Final Complexity**
# - **Time Complexity:** $$ O(N) $$ (each element is visited once)
# - **Space Complexity:** $$ O(N) $$ (set storage)

# ---

# ### **Conclusion**
# If you're getting **TLE**, try these:
# ✅ Use `numSet.remove(n + length)` in the `while` loop.
# ✅ Iterate **over `set(nums)` instead of `nums`**.
# ✅ Try using **PyPy3** on LeetCode.

# Try these fixes and let me know if it's still slow!