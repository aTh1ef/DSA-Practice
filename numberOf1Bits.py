#neetcode 38

class Solution(object):
    def numnberofOneBits(self, n):
        result = 0
        #run the loop till n = 0
        while n:
            # condtion to check if n % 2 gives 1 or 0, if it gives one we add it to the result
            result += n % 2
            #then we shift n right to remove the last digit
            n = n >> 1
        return result

if __name__ == "__main__":
    n = 2147483645
    sol = Solution()
    answer = sol.numnberofOneBits(n)
    print(answer)


# Let's break down the **hammingWeight** function step by step with visualization.

# ### Code Breakdown:
# This function **counts the number of set bits (1s) in the binary representation of a given integer `n`**.

# ---

# ### Given Input:
# Let's take **n = 11** (which is **1011 in binary**).

# ---

# ## **Step-by-step Execution with Visualization**

# ### **Step 1: Initialization**
# ```python
# res = 0
# ```
# - **res** is initialized to **0** (to count the number of 1s).

# ---

# ### **Step 2: First Iteration of `while` Loop**
# ```python
# while n:   # n = 11 (binary: 1011)
#     res += n % 2  # 11 % 2 = 1 → res = 0 + 1 = 1
#     n = n >> 1    # Right shift: 1011 → 101 (binary) = 5
# ```
# - **Checking last bit:** `n % 2` gives **1** (since 11 is odd).
# - **Updating count:** `res = 1`.
# - **Right shift:** `1011` → `101` (binary).

# | Binary Representation | n (decimal) | n % 2 (last bit) | res (count of 1s) | n after shift |
# |-----------------------|-------------|-------------------|--------------------|---------------|
# | **1011**             | 11          | 1                 | 1                  | **101** (5)   |

# ---

# ### **Step 3: Second Iteration**
# ```python
#     res += n % 2  # 5 % 2 = 1 → res = 1 + 1 = 2
#     n = n >> 1    # Right shift: 101 → 10 (binary) = 2
# ```
# - **Checking last bit:** `n % 2` gives **1**.
# - **Updating count:** `res = 2`.
# - **Right shift:** `101` → `10`.

# | Binary Representation | n (decimal) | n % 2 (last bit) | res (count of 1s) | n after shift |
# |-----------------------|-------------|-------------------|--------------------|---------------|
# | **101**              | 5           | 1                 | 2                  | **10** (2)    |

# ---

# ### **Step 4: Third Iteration**
# ```python
#     res += n % 2  # 2 % 2 = 0 → res remains 2
#     n = n >> 1    # Right shift: 10 → 1 (binary) = 1
# ```
# - **Checking last bit:** `n % 2` gives **0** (no change in `res`).
# - **Right shift:** `10` → `1`.

# | Binary Representation | n (decimal) | n % 2 (last bit) | res (count of 1s) | n after shift |
# |-----------------------|-------------|-------------------|--------------------|---------------|
# | **10**               | 2           | 0                 | 2                  | **1** (1)     |

# ---

# ### **Step 5: Fourth Iteration**
# ```python
#     res += n % 2  # 1 % 2 = 1 → res = 2 + 1 = 3
#     n = n >> 1    # Right shift: 1 → 0 (binary) = 0
# ```
# - **Checking last bit:** `n % 2` gives **1**.
# - **Updating count:** `res = 3`.
# - **Right shift:** `1` → `0`.

# | Binary Representation | n (decimal) | n % 2 (last bit) | res (count of 1s) | n after shift |
# |-----------------------|-------------|-------------------|--------------------|---------------|
# | **1**                | 1           | 1                 | 3                  | **0** (0)     |

# ---

# ### **Step 6: Exit the Loop**
# - Now that **n = 0**, the `while` loop stops.
# - The function **returns `res = 3`**, which is the number of **set bits** in `1011`.

# ```python
# return res  # Output: 3
# ```

# ---

# ## **Final Output**
# ```
# Input: n = 11
# Output: 3
# ```
# ✅ The function correctly counts the **three set bits (1s) in 1011**.
