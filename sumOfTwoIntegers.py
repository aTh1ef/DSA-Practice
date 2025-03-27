#leetcode 42
class Solution(object):
    def getSum(self, a, b):
        #first we create a mask so that the answer stays within 32 bits
        MASK = 0xFFFFFFFF
        #run a loop till b is 0
        while b:
            #carry
            temp = (a & b) << 1 & MASK
            #xor
            a = (a ^ b) & MASK
            #update carry
            b = temp & MASK
        return a if a <= 0x7FFFFFFF else ~ (a ^ MASK) #handle negatives

        # cant use this sadge :( return sum([a,b])

# ### **💡 Understanding the Code (Step-by-Step with Visualization)**

# We are implementing addition **without using `+` or `-` operators**, and instead, we rely on **bitwise operations**. The key idea is to use:
# ✅ **Bitwise XOR (`^`)** → Adds numbers without carry.
# ✅ **Bitwise AND (`&`) + Left Shift (`<<`)** → Finds and shifts carry bits.
# ✅ **Masking (`0xFFFFFFFF`)** → Handles Python's unlimited integer size, ensuring **32-bit simulation**.

# ---

# ## **🔢 Example Walkthrough**
# Let's **add `a = 2` and `b = 3`** using the given function.

# ### **Binary Representation**
# ```
# 2  →  00000010
# 3  →  00000011
# ```

# ### **📝 Code with Step-by-Step Explanation & Visualization**
# ---

# ### **Step 1: Initialize the Mask**
# ```python
# MASK = 0xFFFFFFFF  # 32-bit mask
# ```
# ✅ **Why?**
# Python integers are not limited to 32 bits (they can grow indefinitely). To simulate 32-bit numbers (like in C or Java), we use a **bit mask** (`0xFFFFFFFF`).

# 🔍 **Mask Explanation (32-bit binary representation of `MASK`):**
# ```
# 0xFFFFFFFF  =  11111111 11111111 11111111 11111111  (32-bit)
# ```
# ---

# ### **Step 2: Enter the Loop Until `b == 0` (No More Carry)**
# ```python
# while b != 0:
# ```
# ✅ **Why?**
# We keep looping until **`b` (the carry) becomes `0`**, meaning no more carry is left.

# ---

# ### **Step 3: Calculate Carry (`temp = (a & b) << 1`)**
# ```python
# temp = (a & b) << 1
# ```
# ✅ **What Happens?**
# - **Bitwise AND (`&`)** → Identifies bits where both `a` and `b` are `1` (these will generate a carry).
# - **Left Shift (`<< 1`)** → Moves the carry one position left.

# 🔍 **Example (Binary Calculation of Carry)**
# ```
# a  =  00000010   (2)
# b  =  00000011   (3)
# -------------------
# a & b = 00000010   (Only 1s in both)
# (a & b) << 1 = 00000100   (Left shift by 1)
# ```
# ✅ **New Carry (`temp`) = `4` (00000100 in binary)**

# ---

# ### **Step 4: Sum Without Carry (`a = (a ^ b) & MASK`)**
# ```python
# a = (a ^ b) & MASK
# ```
# ✅ **What Happens?**
# - **Bitwise XOR (`^`)** → Adds `a` and `b` **without carrying**.
# - **Masking (`& MASK`)** → Ensures we only keep the **last 32 bits**.

# 🔍 **Example (Binary Calculation of Sum Without Carry)**
# ```
# a  =  00000010   (2)
# b  =  00000011   (3)
# -------------------
# a ^ b = 00000001   (XOR result without carry)
# ```
# ✅ **New `a` = `1` (00000001 in binary)**

# ---

# ### **Step 5: Update Carry (`b = temp & MASK`)**
# ```python
# b = temp & MASK
# ```
# ✅ **What Happens?**
# We update `b` to store only the **carry** (`temp`), ensuring we work within 32-bit limits.

# ✅ **New `b` = `4` (00000100 in binary)**

# 🔍 **Updated Values for Next Iteration:**
# ```
# a = 00000001  (1)
# b = 00000100  (4)
# ```
# Loop continues since `b != 0`.

# ---

# ### **Step 6: Repeat the Loop Until `b == 0`**
# **New Iteration:**
# ```
# a = 00000001   (1)
# b = 00000100   (4)
# ```
# 1. **Calculate Carry:**
#    ```
#    (a & b) = 00000000   (No common bits)
#    (a & b) << 1 = 00000000   (No carry left)
#    ```
#    ✅ `temp = 0` (Carry is now 0)

# 2. **Sum Without Carry:**
#    ```
#    a ^ b = 00000101   (XOR addition)
#    ```
#    ✅ `a = 5` (Binary `00000101`)

# 3. **Update `b`:**
#    ```
#    b = temp & MASK = 00000000
#    ```
#    ✅ `b = 0`, so we exit the loop.

# ---

# ### **Step 7: Handle Negative Numbers (Two's Complement Representation)**
# ```python
# return a if a <= 0x7FFFFFFF else ~(a ^ MASK)
# ```
# ✅ **Why?**
# Python **does not** have a fixed 32-bit integer size. If `a` is greater than `0x7FFFFFFF` (`01111111 11111111 11111111 11111111`), it means it's a **negative number** in a **signed 32-bit system**.
# To **convert to a negative number**, we use **two's complement** representation.

# ---

# ## **Final Output**
# ```
# Input: a = 2, b = 3
# Output: 5
# ```
# ✅ **Binary Check:**
# ```
# 2  →  00000010
# 3  →  00000011
# Sum =  00000101  (5 in binary)
# ```

# ---

# ## **📌 Summary**
# | Step | Operation | Binary Example |
# |------|-----------|----------------|
# | 1️⃣ | Initialize Mask | `MASK = 0xFFFFFFFF` |
# | 2️⃣ | Loop until `b == 0` | `while b != 0:` |
# | 3️⃣ | Compute Carry | `temp = (a & b) << 1` |
# | 4️⃣ | Sum Without Carry | `a = (a ^ b) & MASK` |
# | 5️⃣ | Update Carry | `b = temp & MASK` |
# | 6️⃣ | Check for Negative Numbers | `return a if a <= 0x7FFFFFFF else ~(a ^ MASK)` |

# ---

# ## **🚀 Time & Space Complexity**
# ✅ **Time Complexity:** `O(1)` → At most `32` iterations in a 32-bit system.
# ✅ **Space Complexity:** `O(1)` → No extra space used.

# ---

# ## **🔥 Key Takeaways**
# ✔ **Bitwise XOR (`^`) does addition without carry.**
# ✔ **Bitwise AND (`&`) finds the carry.**
# ✔ **Left Shift (`<<`) moves carry to the correct position.**
# ✔ **Mask (`0xFFFFFFFF`) ensures 32-bit simulation.**
# ✔ **Two's Complement handles negative numbers.**

# 🔹 **This is a clever way to perform addition using bitwise operations!** 🚀

# ### **Understanding `~(a ^ MASK)` in Depth**
# The expression `~(a ^ MASK)` is used to **convert a negative 32-bit integer from unsigned representation back to signed representation** in Python. Let's break it down step by step.

# ---

# ### **1️⃣ What is `MASK = 0xFFFFFFFF`?**
# - `0xFFFFFFFF` is a **32-bit binary mask**:
#   ```
#   0xFFFFFFFF  =  1111 1111 1111 1111 1111 1111 1111 1111  (32-bit)
#   ```
# - It ensures that **only the last 32 bits** of our number are considered, preventing Python from using its default arbitrary-length integers.

# ---

# ### **2️⃣ Why do we use `a ^ MASK`?**
# - The XOR operation (`^`) inverts all bits:
#   ```
#   a ^ MASK   →  Flips all bits of `a`
#   ```
# - If `a` is stored in **32-bit unsigned representation**, `a ^ MASK` flips it into a **signed negative representation**.

# #### **Example:**
# Let's say `a = 0b11111111111111111111111111111110` (which is `4294967294` in unsigned form).
# If we do:
# ```python
# a ^ MASK
# ```
# We get:
# ```
# 0b00000000000000000000000000000001  (which is just `1`)
# ```
# But it's still in unsigned form.

# ---

# ### **3️⃣ Why `~(a ^ MASK)`?**
# - The `~` (bitwise NOT) **flips the bits again**, converting `a` into a signed negative integer.

# #### **Example:**
# If `a ^ MASK = 1`,
# `~1 = -2` (because in Python, `~x = -x - 1`).

# So, `~(a ^ MASK)` ensures that numbers that were negative in a **32-bit system** are properly represented in **Python's signed integers**.

# ---

# ### **4️⃣ Why do we need this conversion?**
# - Python **does not** have a fixed integer size.
# - However, languages like **C++ or Java use 32-bit signed integers**.
# - This operation **mimics how negative numbers are stored in a 32-bit system**.

# ---

# ### **📌 Summary**
# ✅ `a ^ MASK` → Flips bits to get a **positive representation** of a negative number.
# ✅ `~(a ^ MASK)` → Converts it back to **a proper signed negative integer**.

# ### **🔥 Final Example**
# ```python
# a = 0xFFFFFFFE  # This is -2 in a 32-bit signed system
# MASK = 0xFFFFFFFF

# print(~(a ^ MASK))  # Output: -2
# ```

# Now you can **safely work with negative numbers in a 32-bit environment**! 🚀