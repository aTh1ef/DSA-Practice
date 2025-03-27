#neetcode 40
class Solution:
    def reverseBits(self, n):
        #defining a variable to store the answer
        result = 0
        #looping through 32 bits because we are suppose to reverse 32 bits
        for i in range(32):
            # here we shift right from the ith bits which is 0 and go on till 32 and also & operate it by 1
            bits = (n >> i) & 1
            #we move the bits from the left most to the right most
            result += bits << (31 - i)
        return result

# ## **Code: Reverse Bits in Python**
# ```python
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0  # Step 1: Initialize result as 0
#         for i in range(8):  # Step 2: Loop through 8 bits (for simplicity)
#             bit = (n >> i) & 1  # Step 3: Extract the rightmost bit
#             res += (bit << (7 - i))  # Step 4: Move it to the reversed position
#         return res  # Step 5: Return the final reversed number

# # Example usage:
# n = 0b10110010  # Binary representation of our number
# solution = Solution()
# result = solution.reverseBits(n)
# print(bin(result))  # Output should be 0b01001101
# ```
# ---

# ## **🔎 Step-by-Step Breakdown**
# Let's **visualize** this process with **each step of the loop**.

# ---

# ### **🌟 Step 1: Initialize `res = 0`**
# ```python
# res = 0
# ```
# **🔍 Visualization:**
# ```
# n    = 10110010  (Original number)
# res  = 00000000  (This will store the reversed bits)
# ```

# ---

# ### **🔄 Step 2: Loop through Each Bit (8 iterations)**
# ```python
# for i in range(8):
# ```
# We **go from `i = 0` to `i = 7`** (because we're working with 8 bits).

# ---

# ### **🔢 Step 3: Extract the Rightmost Bit**
# ```python
# bit = (n >> i) & 1
# ```
# - `n >> i` → **Shifts** the number `i` times to the right.
# - `& 1` → **Extracts** the last bit.

# ---

# ### **🛠 Step 4: Move the Extracted Bit to the Correct Position**
# ```python
# res += (bit << (7 - i))
# ```
# - `bit << (7 - i)` moves the bit to the **correct place** in `res`.
# - `+=` adds it to `res`.

# ---

# ### **🖼 Visualization of Each Loop Iteration**
# Let's break down **each step** and **show what happens** to `res`.

# | `i`  | Extracted Bit (`bit = (n >> i) & 1`) | Moved to Position `(7 - i)` | `res` After Adding |
# |------|-------------------------------------|----------------------------|--------------------|
# | 0    | **0** (rightmost)                   | Position **7**              | `00000000`        |
# | 1    | **1**                               | Position **6**              | `01000000`        |
# | 2    | **0**                               | Position **5**              | `01000000`        |
# | 3    | **0**                               | Position **4**              | `01000000`        |
# | 4    | **1**                               | Position **3**              | `01001000`        |
# | 5    | **1**                               | Position **2**              | `01001100`        |
# | 6    | **0**                               | Position **1**              | `01001100`        |
# | 7    | **1** (leftmost)                    | Position **0**              | `01001101`        |

# ---

# ### **🎯 Final Output**
# ```python
# return res
# ```
# **`res` now holds** the **reversed** version of `n`:
# ```
# Input:  10110010  (original)
# Output: 01001101  (reversed)
# ```

# ✅ **Final Output in Binary**: `0b01001101`
# ✅ **Final Output in Decimal**: `77`

# ---

# ### **🔥 TL;DR (Too Long; Didn't Read)**
# 1️⃣ Start with `res = 0`.
# 2️⃣ **Loop** through 8 bits (or 32 if full version).
# 3️⃣ **Extract each bit** from the right side of `n`.
# 4️⃣ **Move it to the correct left position** in `res`.
# 5️⃣ Return `res`, which now has the **reversed** bits.