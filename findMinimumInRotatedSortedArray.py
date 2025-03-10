#neetcode!7
class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        result = nums[0]

        # Checking if the loop is sorted, so if the left index's element is shorter than the right index's element it means it is sorted and then we break the loop
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            # Now in this loop we  set a middle element and check if the middle elemnet is greater than or equal to the left most element and if it is we know that the minimum element is at the right side of the array if not we check the left side of the array
            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result

if __name__ == "__main__":
    nums = [3,4,5,6,1,2]
    sol = Solution()
    answer = sol.findMin(nums)
    print(answer)


# I'm gonna break this thing **line by line**, **concept by concept**, as if I'm explaining it to someone who's totally new. You ready? Let's roll! 🚀

# ---

# ## 📦 What's This Code Doing?

# This code is trying to **find the smallest number** (minimum) in a **rotated sorted array**.

# Example of a rotated sorted array:
# ```
# Original sorted array: [1, 2, 3, 4, 5, 6, 7]
# Rotated sorted array: [4, 5, 6, 7, 1, 2, 3]
# ```
# We need to find the **minimum element** (`1` in this example), and we do it **without** going through every single number. We use **binary search**, which makes it much faster.

# ---

# ## 🔨 Step-by-Step Code Breakdown (Like I'm Explaining to Myself)

# ```python
# class Solution:
# ```
# - We're making a **blueprint** (class) called `Solution`. It's just a container for our method (function).

# ```python
#     def findMin(self, nums: List[int]) -> int:
# ```
# - Inside our `Solution` class, we make a **function** called `findMin`.
# - It accepts `nums`, which is the **list of numbers** (our rotated sorted array).
# - `List[int]` means the input is a list of integers.
# - It will **return an integer**, the smallest number in the list.

# ---

# ## 🚀 The Core Logic Begins!

# ### Line 1
# ```python
#         res = nums[0]
# ```
# - We start by assuming the **first number** in the array (`nums[0]`) is the **smallest**.
# - `res` holds the **current smallest number we've seen so far**.

# ---

# ### Line 2
# ```python
#         l, r = 0, len(nums) - 1
# ```
# - `l` is the **left pointer**, starting at index `0` (beginning of the array).
# - `r` is the **right pointer**, starting at the **last index** (`len(nums) - 1`).

# Imagine your array is:
# ```
# [4, 5, 6, 7, 1, 2, 3]
# ```
# - `l = 0` points at `4`.
# - `r = 6` points at `3`.

# ---

# ## 🔁 Time to Loop! (While Loop)

# ```python
#         while l <= r:
# ```
# - We are going to keep looping **while left is less than or equal to right**.
# - This ensures we are still looking at a valid portion of the array.

# ---

# ### First Check Inside the Loop
# ```python
#             if nums[l] < nums[r]:
# ```
# - **What are we checking?**
#   If the **left number** is **less than the right number**.

# - **Why?**
#   If this happens, it means the **current portion of the array is already sorted**, so the smallest number must be at `nums[l]`.

# Example:
# ```
# If nums[l] = 1 and nums[r] = 3 (like in [1, 2, 3])
# The whole thing is sorted, and `1` is the smallest.
# ```

# ---

# ### Update the Result
# ```python
#                 res = min(res, nums[l])
# ```
# - We take the **smaller** of `res` and `nums[l]`.
# - `res` is keeping track of the **smallest number we've found so far**.

# ---

# ### Break If Already Sorted
# ```python
#                 break
# ```
# - If we just found a **sorted chunk**, and we updated `res`, there's **no need to keep looking**, so we **break out** of the loop.

# ---

# ## 🧠 Now We Go Binary Search Mode
# If the array isn't sorted, we have to go deeper!

# ### Find the Middle
# ```python
#             m = (l + r) // 2
# ```
# - We find the **middle index** between `l` and `r`.
# - `// 2` just means **integer division** (we don't want decimal numbers).
# - Think of `m` as our **middle finger**, pointing at the middle of our search area!

# Example:
# ```
# l = 0 (pointing at 4)
# r = 6 (pointing at 3)
# m = (0 + 6) // 2 = 3
# nums[m] = 7
# ```

# ---

# ### Update the Result with the Middle Element
# ```python
#             res = min(res, nums[m])
# ```
# - We compare the **current smallest** (`res`) with `nums[m]` (middle value).
# - `min()` picks the **smaller one**.

# ---

# ### Now Decide Where to Search Next
# ```python
#             if nums[m] >= nums[l]:
# ```
# - **What are we checking?**
#   Is the middle value `nums[m]` **greater than or equal to** the left value `nums[l]`?

# - **Why?**
#   If the middle is bigger, it means the **smallest number is in the right half**.
#   The left side (from `l` to `m`) is **sorted**, and the minimum can't be there (we've already checked).

# Example:
# ```
# nums[m] = 7
# nums[l] = 4
# Since 7 >= 4, we search the **right half**.
# ```

# ---

# ### Move the Left Pointer
# ```python
#                 l = m + 1
# ```
# - We **shift the left pointer** to `m + 1`.
# - We're ignoring the left side, and moving our search to the **right half**.

# ---

# ### Else: Search Left Half
# ```python
#             else:
#                 r = m - 1
# ```
# - If `nums[m]` **isn't** greater than `nums[l]`,
#   It means the **smallest number is on the left half**,
#   So we **shift the right pointer** to `m - 1`.

# ---

# ## ✅ After the Loop Ends...
# ```python
#         return res
# ```
# - `res` now holds the **smallest number** we found!
# - We **return** it!

# ---

# ## 👁️‍🗨️ Let's Walk Through a Full Example

# Array:
# ```
# [4, 5, 6, 7, 0, 1, 2]
# ```
# - `res = 4`
# - `l = 0`
# - `r = 6`

# ### First Loop:
# - `nums[l] = 4`
# - `nums[r] = 2`
# - `nums[l]` is **not** less than `nums[r]`, so keep going.

# - `m = (0 + 6) // 2 = 3`
# - `nums[m] = 7`
# - `res = min(4, 7) = 4`
# - Since `nums[m] = 7 >= nums[l] = 4`,
#   Move `l` to `m + 1 = 4`.

# ### Second Loop:
# - `l = 4`, `r = 6`
# - `nums[l] = 0`
# - `nums[r] = 2`
# - `nums[l] < nums[r]`!
#   This means **sorted chunk**.
# - `res = min(4, 0) = 0`
# - Break out of the loop.

# ### Return `res = 0`.

# ---

# ## 🌟 What Did We Do?
# We found `0`, the **smallest number**, in **logarithmic time** (`O(log n)`), by using **binary search** instead of going one by one.

# ---

# ## ✨ Super Simple Visualization
# Imagine a **pizza slice**.
# - The crust side is sorted.
# - But the **cheese dripped down and rotated the slice**!
# - You keep **cutting the slice in half**, checking which side is lower.
# - You find the **cheesiest, lowest point** — that's your **minimum**.

# ---

# ## 🧠 Key Takeaways:
# 1. We're finding the **smallest number in a rotated sorted array**.
# 2. We use **binary search** to cut down the time.
# 3. We **compare** the left, middle, and right to decide where to search next.
# 4. **Efficiency**: `O(log n)` time instead of `O(n)`.


