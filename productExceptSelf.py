#neetcode 7
class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    answer = sol.productExceptSelf(nums)
    print(answer)


# Below is the **entire code** (in Python) that solves the "Product of Array Except Self" problem, followed by a **line-by-line** breakdown in the simplest terms possible—like you're explaining it to someone who's brand new (or, as you said, a "dumbass," but we'll just say "super-newbie"!). We'll also include a **visual** walkthrough so you can really see what's happening at each step.

# ---

# ## The Code

# ```python
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # 1) Create an output array 'res' filled with 1s, same size as 'nums'
#         res = [1] * len(nums)
#
#         # 2) Calculate prefix products and store them in 'res'
#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#
#         # 3) Calculate postfix products and multiply them into 'res'
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#
#         # 4) Return the final result
#         return res
# ```

# ---

# ## Line-by-Line Explanation

# ### 1. `class Solution:`
# - We're defining a class named `Solution`. This is just a container for our function (a common pattern in coding interview platforms like LeetCode).

# ### 2. `def productExceptSelf(self, nums: List[int]) -> List[int]:`
# - We define a function called `productExceptSelf`.
# - It takes a list of integers `nums` as input and promises to return another list of integers.

# ### 3. `res = [1] * len(nums)`
# - We create a list called `res` (short for "result").
# - It's initially filled with `1` for every position in `nums`.
# - If `nums` has 5 elements, `res` will be `[1, 1, 1, 1, 1]`.
# - Why start with 1? Because 1 is the neutral element for multiplication (like how 0 is for addition).

# ### 4. `prefix = 1`
# - `prefix` will keep track of the product of all elements **before** the current index as we loop from left to right.
# - Starting it at 1 means "we haven't multiplied anything yet."

# ### 5. `for i in range(len(nums)):`
# - We're going to loop through the array from the first element (index 0) to the last element (index `len(nums)-1`).

# ### 6. `res[i] = prefix`
# - For each index `i`, we set `res[i]` to whatever `prefix` currently is.
# - This means "the product of everything before `nums[i]`."
# - Initially, `prefix` is 1, so `res[0]` becomes 1. That makes sense, because for the first element, there's nothing before it, so the product of "no elements" is 1.

# ### 7. `prefix *= nums[i]`
# - We update `prefix` by multiplying it with the current element `nums[i]`.
# - This means for the **next** position in the loop, `prefix` will represent the product of all the elements up to the current index.

# *(By the time we finish this loop, `res[i]` holds the product of all elements to the **left** of index `i`.)*

# ### 8. `postfix = 1`
# - We define a new variable `postfix`.
# - Similar to `prefix`, but this one will handle the product of all elements **after** the current index.
# - We'll fill this in by looping from right to left.

# ### 9. `for i in range(len(nums) - 1, -1, -1):`
# - This loop goes backwards from the last index (`len(nums) - 1`) down to 0.
# - Example: if `len(nums)` is 5, this loop goes `i = 4, 3, 2, 1, 0`.

# ### 10. `res[i] *= postfix`
# - We multiply the current value of `res[i]` by `postfix`.
# - Remember, `res[i]` already holds the product of all elements to the left.
# - By multiplying with `postfix`, we now also include the product of all elements to the right.
# - So after this line, `res[i]` = product of everything except `nums[i]`.

# ### 11. `postfix *= nums[i]`
# - We then update `postfix` by multiplying it by the current element `nums[i]`.
# - This sets `postfix` up for the next iteration, so it correctly represents the product of all elements to the right of the **next** index as we move leftward.

# ### 12. `return res`
# - Finally, we return `res`.
# - `res` now has the product of all elements except the one at each index, for every index in the array.

# ---

# ## Visualization Example

# Let's walk through a simple example: `nums = [1, 2, 3, 4]`.

# 1. **Initialize**:
#    - `res = [1, 1, 1, 1]`
#    - `prefix = 1`
#    - `postfix = 1` (we'll use it later)

# 2. **First loop (prefix pass)**:
#    - **i = 0**:
#      - `res[0] = prefix` → `res[0] = 1`
#      - `prefix *= nums[0]` → `prefix = 1 * 1 = 1`
#      - Now, `res = [1, 1, 1, 1]`, `prefix = 1`
#    - **i = 1**:
#      - `res[1] = prefix` → `res[1] = 1`
#      - `prefix *= nums[1]` → `prefix = 1 * 2 = 2`
#      - Now, `res = [1, 1, 1, 1]`, `prefix = 2`
#    - **i = 2**:
#      - `res[2] = prefix` → `res[2] = 2`
#      - `prefix *= nums[2]` → `prefix = 2 * 3 = 6`
#      - Now, `res = [1, 1, 2, 1]`, `prefix = 6`
#    - **i = 3**:
#      - `res[3] = prefix` → `res[3] = 6`
#      - `prefix *= nums[3]` → `prefix = 6 * 4 = 24`
#      - Now, `res = [1, 1, 2, 6]`, `prefix = 24`

#    After this loop, `res` says:
#    - At index 0 → 1 (product of nothing to the left)
#    - At index 1 → 1 (product of just the element `nums[0]` = 1)
#    - At index 2 → 2 (product of `nums[0]` and `nums[1]` = 1*2)
#    - At index 3 → 6 (product of `nums[0]`, `nums[1]`, `nums[2]` = 1*2*3)

# 3. **Second loop (postfix pass)**:
#    - We go from right to left now:
#    - **i = 3**:
#      - `res[3] *= postfix` → `res[3] = 6 * 1 = 6`
#      - `postfix *= nums[3]` → `postfix = 1 * 4 = 4`
#      - Now, `res = [1, 1, 2, 6]`, `postfix = 4`
#    - **i = 2**:
#      - `res[2] *= postfix` → `res[2] = 2 * 4 = 8`
#      - `postfix *= nums[2]` → `postfix = 4 * 3 = 12`
#      - Now, `res = [1, 1, 8, 6]`, `postfix = 12`
#    - **i = 1**:
#      - `res[1] *= postfix` → `res[1] = 1 * 12 = 12`
#      - `postfix *= nums[1]` → `postfix = 12 * 2 = 24`
#      - Now, `res = [1, 12, 8, 6]`, `postfix = 24`
#    - **i = 0**:
#      - `res[0] *= postfix` → `res[0] = 1 * 24 = 24`
#      - `postfix *= nums[0]` → `postfix = 24 * 1 = 24`
#      - Now, `res = [24, 12, 8, 6]`, `postfix = 24`

# 4. **Final result**:
#    - `res = [24, 12, 8, 6]`
#    - Check it:
#      - The product of everything except `nums[0]` (which is 1) is `2 * 3 * 4 = 24`.
#      - Except `nums[1]` (which is 2) is `1 * 3 * 4 = 12`.
#      - Except `nums[2]` (which is 3) is `1 * 2 * 4 = 8`.
#      - Except `nums[3]` (which is 4) is `1 * 2 * 3 = 6`.
#    - Perfect!

# ---

# ## Why This Works

# - **Prefix** captures all the stuff to the left.
# - **Postfix** captures all the stuff to the right.
# - By multiplying the prefix and postfix values together, we get the product of everything **except** the current element—without ever using division.
#
# ---

# ## In the Most Basic Terms

# 1. You first go left-to-right, collecting the product of all numbers before each index (that's `prefix`).
# 2. Then you go right-to-left, collecting the product of all numbers after each index (that's `postfix`).
# 3. Combine (multiply) those two products for each position, and boom—your result is the product of all numbers **except** the one at the current position.

# That's it! You're done, and hopefully it wasn't too painful.