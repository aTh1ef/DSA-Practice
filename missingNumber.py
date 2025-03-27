#neetcode 41
class Solution(object):
    def missingNumber(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

        # alternate answer but time complexity is o(n) and space complexity is o(1)
        # count = {}
        # for n in nums:
        #         count[n] = True

        # for i in range(len(nums) + 1):
        #     if i not in count:
        #         return i

# Let's break down the given Python code **step by step** with **explanations and visualization**.
#
# ---
#
# ## **📌 Understanding the Code**
# This function **finds the missing number** in an array containing numbers from `0` to `n`, with one number missing.
#
# ```python
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)  # Step 1: Initialize res with n (length of nums)
#
#         for i in range(len(nums)):  # Step 2: Loop through the indices
#             res += (i - nums[i])  # Step 3: Adjust res by adding (i - nums[i])
#
#         return res  # Step 4: Return the missing number
# ```
#
# ---
#
# ## **🔢 Example Walkthrough**
# Let's take an example:
#
# ### **📝 Input:**
# ```python
# nums = [3, 0, 1]
# ```
# (The missing number is `2` because the numbers should be `[0, 1, 2, 3]`.)
#
# ---
#
# ### **🛠 Step-by-Step Execution**
#
# #### **Step 1️⃣: Initialize `res`**
# ```python
# res = len(nums)  # res = 3
# ```
# 📌 Since `nums` contains 3 elements (`[3, 0, 1]`), `len(nums) = 3`.
# So, `res = 3` (initially set to `n`, the length of the list).
#
# ---
#
# #### **Step 2️⃣: Start Looping**
# ```python
# for i in range(len(nums)):  # i iterates from 0 to 2
# ```
# 🔹 We iterate over **each index `i`** and **each number `nums[i]`**.
#
# | Iteration | `i` (Index) | `nums[i]` (Number) | `i - nums[i]` | `res += (i - nums[i])` | `res` (Updated) |
# |-----------|------------|-------------------|--------------|---------------------|----------------|
# | **0**     | `0`        | `3`               | `0 - 3 = -3`  | `3 + (-3) = 0`      | `0`            |
# | **1**     | `1`        | `0`               | `1 - 0 = 1`   | `0 + 1 = 1`        | `1`            |
# | **2**     | `2`        | `1`               | `2 - 1 = 1`   | `1 + 1 = 2`        | `2`            |
#
# ---
#
# #### **Step 3️⃣: Return the Final Value**
# ```python
# return res  # Returns 2
# ```
# ✅ The function correctly **returns `2`**, which is the missing number.
#
# ---
#
# ## **📌 Visualization**
# Let's visualize how `res` changes in each step:
#
# ```
# Initial res = n = 3
#
# Iteration 1: i = 0, nums[i] = 3
#    res = 3 + (0 - 3) = 3 - 3 = 0
#
# Iteration 2: i = 1, nums[i] = 0
#    res = 0 + (1 - 0) = 0 + 1 = 1
#
# Iteration 3: i = 2, nums[i] = 1
#    res = 1 + (2 - 1) = 1 + 1 = 2
#
# Final res = 2  ✅ (Correct missing number)
# ```
#
# ---
#
# ## **⏱ Complexity Analysis**
# - **Time Complexity:** `O(n)` (Single loop)
# - **Space Complexity:** `O(1)` (No extra space used)
#
# ---
#
# ## **🔥 Summary**
# ✔ **Simple and elegant** approach
# ✔ **Avoids extra memory (`O(1) space`)**
# ✔ **Runs efficiently in `O(n)` time**
# ✔ **Uses mathematical trick (`i - nums[i]`) to track the missing number**

