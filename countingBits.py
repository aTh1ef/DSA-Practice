#neetcode 39

class Solution(object):
    def countBits(self, n):
        #create a list of zeroes that go till n + 1
        res = [0] * (n + 1)
        #create a loop that will go from index 1 to n + 1 because 0th index's value is 0 which is already in binary
        for i in range(1, n + 1):
            res[i] = res[i // 2] + i % 2
        return res

# ## **🚀 Understanding the `countBits(n)` Function Step by Step**
# We're building an array where each index `i` represents the **number of 1's in its binary representation**.

# ```python
# def countBits(n):
#     ans = [0] * (n + 1)  # Step 1: Create an array filled with 0s
# ```
# ### **👀 Step 1: Creating the Answer Array**
# We make an array of size **(n + 1)** filled with `0`s.
# If `n = 5`, we get:

# ```
# ans = [0, 0, 0, 0, 0, 0]  # This will store the final answer
#        0  1  2  3  4  5  (Indexes)
# ```
# Each index represents a number, and we will **fill in the correct number of `1`s in binary** as we go.

# ---

# ```python
#     for i in range(1, n + 1):  # Step 2: Start looping from 1 to n
# ```
# ### **🔄 Step 2: Looping Through Numbers**
# We loop from `1` to `n`, checking each number's **binary representation**.

# - We don't need to check `0` because we already know that `0` in binary is `0` (so it has 0 ones).

# ---

# ```python
#         ans[i] = ans[i // 2] + (i % 2)  # Step 3: Fill in the ans array
# ```
# ### **🤯 Step 3: Using the Magic Formula**
# This is the key formula:

# \[
# \text{ans}[i] = \text{ans}[i // 2] + (i \% 2)
# \]

# **Let's break it down:**
# - **`ans[i // 2]`** → This gives the count of `1`s in the **previous number** (without the last bit).
# - **`(i % 2)`** → This checks if the last bit is `1` or `0`:
#   - If `i` is **even**, last bit = `0`
#   - If `i` is **odd**, last bit = `1` (so we add 1).

# ---

# ## **💡 Full Walkthrough with Example (n = 5)**

# ### **📌 Initial State**
# ```
# ans = [0, 0, 0, 0, 0, 0]  # All 0s initially
# ```

# ---

# ### **Step-by-Step Execution**
# 🔹 **For `i = 1` (Binary: `1`)**
# ```python
# ans[1] = ans[1 // 2] + (1 % 2)
#        = ans[0] + 1
#        = 0 + 1
#        = 1
# ```
# **Updated Array:**
# ```
# ans = [0, 1, 0, 0, 0, 0]
# ```
# 🧐 **Why?**
# - `1` in binary is `1` → **Only one `1`**.

# ---

# 🔹 **For `i = 2` (Binary: `10`)**
# ```python
# ans[2] = ans[2 // 2] + (2 % 2)
#        = ans[1] + 0
#        = 1 + 0
#        = 1
# ```
# **Updated Array:**
# ```
# ans = [0, 1, 1, 0, 0, 0]
# ```
# 🧐 **Why?**
# - `2` in binary is `10` → **Only one `1`**.

# ---

# 🔹 **For `i = 3` (Binary: `11`)**
# ```python
# ans[3] = ans[3 // 2] + (3 % 2)
#        = ans[1] + 1
#        = 1 + 1
#        = 2
# ```
# **Updated Array:**
# ```
# ans = [0, 1, 1, 2, 0, 0]
# ```
# 🧐 **Why?**
# - `3` in binary is `11` → **Two `1`s**.

# ---

# 🔹 **For `i = 4` (Binary: `100`)**
# ```python
# ans[4] = ans[4 // 2] + (4 % 2)
#        = ans[2] + 0
#        = 1 + 0
#        = 1
# ```
# **Updated Array:**
# ```
# ans = [0, 1, 1, 2, 1, 0]
# ```
# 🧐 **Why?**
# - `4` in binary is `100` → **Only one `1`**.

# ---

# 🔹 **For `i = 5` (Binary: `101`)**
# ```python
# ans[5] = ans[5 // 2] + (5 % 2)
#        = ans[2] + 1
#        = 1 + 1
#        = 2
# ```
# **Updated Array:**
# ```
# ans = [0, 1, 1, 2, 1, 2]
# ```
# 🧐 **Why?**
# - `5` in binary is `101` → **Two `1`s**.

# ---

# ## **Final Answer for `n = 5`**
# ```python
# [0, 1, 1, 2, 1, 2]
# ```
# 🎯 **Boom! Done!** 🎯

# ---

# ## **⏱️ Time Complexity Analysis**
# ### **How Efficient is This?**
# - **Each number is processed once** → **O(n)**
# - **Only basic operations (`//`, `%`, `+`)** → **O(1) per step**
# - **Overall Complexity: O(n)** ✅ **(Very Fast!)**

# ---

# ## **🎯 Why This is Better Than O(n log n)**
# - A brute force method (checking every bit manually) would be **O(n log n)**.
# - Our approach **only depends on previous results**, making it **O(n)**, which is super efficient.

# ---

# ## **🔥 TL;DR (Too Long; Didn't Read)**
# 1. **Make an array** of size `(n + 1)` filled with `0`s.
# 2. **Loop from `1` to `n`** and calculate the number of `1`s using:
#    \[
#    \text{ans}[i] = \text{ans}[i // 2] + (i \% 2)
#    \]
# 3. **Fill the array step by step** based on previously computed results.
# 4. **Final answer = `[0, 1, 1, 2, 1, 2]`** (for `n = 5`).
# 5. **Super efficient (O(n) time complexity)**.

# ---

# ## **🎉 Conclusion**
# ✅ **Now you understand this like a pro!**
# ✅ **You got code + visualization + deep dive!**