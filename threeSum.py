#leetcode 10
#threeSum
class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    answer = sol.threeSum(nums)
    print(answer)

Thought for 2 seconds```python
# Below is the **exact same code** we're discussing, followed by a **line-by-line breakdown** in **very plain, everyday language**—like explaining to someone completely new to coding. I'll try to be as thorough and clear as possible.

# ---

# ## The Code

# ```python
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1

#         return res
# ```

# ---

# ## Understanding It Step by Step

# ### 1. `class Solution:`
# - We're defining a **class** called `Solution`.
# - In many coding interview problems, especially on platforms like LeetCode, you wrap your solution in a class named `Solution`.

# ### 2. `def threeSum(self, nums: List[int]) -> List[List[int]]:`
# - Inside the `Solution` class, we define a **function** (method) called `threeSum`.
# - It takes one argument, `nums`, which is a list of integers (`List[int]` is just a **type hint**—it tells us that `nums` is expected to be a list of integers).
# - The arrow `-> List[List[int]]` means this function is expected to **return** a list of lists of integers. In other words, something like `[[x1, y1, z1], [x2, y2, z2], ...]`.

# ### 3. `res = []`
# - We create an empty list called `res`.
# - This will be our **result list** where we store all the **triplets** that add up to zero (the main goal of the 3Sum problem).

# ### 4. `nums.sort()`
# - We **sort** the list `nums` in ascending order (smallest to largest).
# - Sorting helps us more easily avoid duplicates and use the two-pointer approach.

# ### 5. `for i, a in enumerate(nums):`
# - We loop over each element in the sorted list using `enumerate`.
# - `i` will be the **index** (0, 1, 2, ...) and `a` will be the **actual number** at that position in `nums`.
# - Essentially, we're saying: "For each position `i` in `nums`, let `a` be `nums[i]`."

# ### 6. `if i > 0 and a == nums[i - 1]:`
# ### 7. `    continue`
# - These two lines say:
#   - If `i > 0` (meaning we're **not** at the very first element) **and** the current number `a` is the **same** as the previous number (`nums[i - 1]`), then **skip** this iteration.
# - Why do we skip?
#   - **We don't want to find the same triplet more than once.** If `nums[i]` is the same as `nums[i - 1]`, that means we'd be re-checking the same number again and would probably generate duplicate triplets. So we `continue` (jump to the next loop iteration).

# ### 8. `l, r = i + 1, len(nums) - 1`
# - We set up **two pointers**:
#   - `l` (left pointer) starts just one position to the right of `i` (`i + 1`).
#   - `r` (right pointer) starts at the very end of the list (`len(nums) - 1`).
# - The idea is to **narrow** these two pointers inward to find combinations that sum to zero.

# ### 9. `while l < r:`
# - We begin a **while loop** that keeps going **as long as** the left pointer is still to the left of the right pointer (`l < r`).
# - This is the classic "two-pointer" technique.

# ### 10. `threeSum = a + nums[l] + nums[r]`
# - We calculate the sum of three numbers:
#   1. The current number we picked in the `for` loop (`a`),
#   2. The number at the left pointer (`nums[l]`),
#   3. The number at the right pointer (`nums[r]`).
# - We store this sum in a variable called `threeSum`.

# ### 11. `if threeSum > 0:`
# ### 12. `    r -= 1`
# - If the sum of these three numbers is **greater than zero**, it means we're too "heavy" or "large" on the right side.
# - We reduce the sum by moving the **right pointer** one step to the left (`r -= 1`) to try to get a smaller number.

# ### 13. `elif threeSum < 0:`
# ### 14. `    l += 1`
# - If the sum is **less than zero**, it means we need a **bigger** number to reach zero.
# - We move the **left pointer** one step to the right (`l += 1`) to try to get a larger number.

# ### 15. `else:`
# - The `else` here catches the case when `threeSum == 0`.
# - That means we've found a **perfect combination**: `a + nums[l] + nums[r] = 0`.

# ### 16. `res.append([a, nums[l], nums[r]])`
# - We **append** this triplet `[a, nums[l], nums[r]]` to our results list `res`.
# - This means we've successfully found three numbers that sum to zero.

# ### 17. `l += 1`
# - We move the **left pointer** to the right by one to look for any other possible triplets.
# - We don't move the right pointer here, but we could move it in the loop if needed.

# ### 18. `while nums[l] == nums[l - 1] and l < r:`
# ### 19. `    l += 1`
# - After finding a valid triplet, we want to **skip over any duplicate numbers** at the left pointer, because we don't want to list the **same** triplet more than once.
# - So we say: "While the new `nums[l]` is the same as the old `nums[l - 1]`, keep moving `l` to the right."
# - This ensures we don't generate duplicate triplets like `[1,2,-3]` multiple times just because we had repeated `2`s in the list.

# ### 20. `return res`
# - Once the loop finishes (we've tried all possible i, l, r combinations), we **return** the `res` list, which contains **all unique triplets** that sum to zero.

# ---

# ## Big Picture Explanation

# 1. **Sort the List**: We start by sorting the numbers. This makes it easier to avoid duplicates and use the two-pointer approach.
# 2. **Loop Through Each Number**: We pick a number `a` at index `i`.
# 3. **Skip Duplicates**: If we've already used a number identical to `a` at position `i-1`, we skip it.
# 4. **Two-Pointer Magic**:
#    - We set a left pointer `l` right after `i`.
#    - We set a right pointer `r` at the end of the list.
#    - We calculate the sum of the three numbers: `a`, `nums[l]`, and `nums[r]`.
#    - If the sum is **too big** (> 0), we move `r` left to reduce the sum.
#    - If the sum is **too small** (< 0), we move `l` right to increase the sum.
#    - If the sum is **exactly zero**, we add that triplet to our results. Then we move `l` to skip duplicates.
# 5. **Continue Until All Possibilities Are Checked**: We do this for every `i`, moving the pointers around, until we've covered all potential triplets.
# 6. **Return the Results**: We give back a list of all the triplets that add up to zero.

# ---

# ## Visualizing a Simple Example

# Let's say our `nums` list is `[ -1, 0, 1, 2, -1, -4 ]`.

# 1. **Sort** it → `[-4, -1, -1, 0, 1, 2]`
# 2. **Pick `i=0`, `a=-4`**:
#    - `l=1`, `r=5`
#    - Check sums with `-4, -1, 2`, then `-4, -1, 1`, etc., until `l < r` no longer holds. If we find zero, store it.
# 3. **Pick `i=1`, `a=-1`**:
#    - `l=2`, `r=5`
#    - Check sums.
#    - If sum is too big, move `r`.
#    - If sum is too small, move `l`.
#    - If sum is zero, store that triplet. Then skip duplicates.
# 4. Continue for all `i`.

# In the end, we'd discover triplets like `[-1, -1, 2]` and `[-1, 0, 1]` which both sum to 0.

# ---

# ## Why This Works

# - **Sorting** + **Two Pointers** is a common pattern:
#   - Sorting lets us move the `l` and `r` pointers in a predictable way (smaller numbers on the left, bigger numbers on the right).
#   - We can systematically "shrink" or "expand" our search window based on whether the sum is too big or too small.
# - **Avoiding duplicates** is handled by:
#   - Skipping the same `i` if it matches the previous number.
#   - Skipping repeated numbers after we've found a valid triplet by advancing `l` while `nums[l] == nums[l - 1]`.

# ---

# ## Final Thoughts

# - This approach has a time complexity of roughly **O(n^2)**, because for each `i` (that's `n` times), we use a two-pointer approach that can scan through the list in about `O(n)` in the worst case.
# - The solution is **efficient** enough for most typical constraints on the 3Sum problem (like `n` up to a few thousand).

# ---

# ### In Summary (Super Plain Terms)

# 1. **Sort** the list so it's easy to handle.
# 2. **Loop** through each number:
#    - Skip it if it's the same as the one we just checked (no duplicates).
#    - Use two markers (left and right) to try to find two other numbers that, together with the current number, add up to zero.
#    - If the sum is too big, move the right marker left (to try smaller numbers).
#    - If the sum is too small, move the left marker right (to try bigger numbers).
#    - If the sum is zero, record that trio and skip any repeats.
# 3. **Give back** all the unique trios that sum to zero.

# That's it. This is a **classic** algorithmic problem, and this code is a neat, clean solution using sorting and the two-pointer technique.
```


# Yes! We **can** use `for i in range(len(nums))` instead of `enumerate(nums)`. The main reason for using `enumerate(nums)` is convenience, but both approaches work.

# ### **Current Code Using `enumerate`**
# ```python
# for i, a in enumerate(nums):
# ```
# - `enumerate(nums)` gives **both** the index (`i`) and the value (`a`) in `nums`.
# - So, inside the loop, `a` is just `nums[i]`, but it's more convenient since we don't have to write `nums[i]` explicitly.

# ### **Alternative: Using `for i in range(len(nums))`**
# ```python
# for i in range(len(nums)):
#     a = nums[i]  # Manually get the value
# ```
# - Instead of directly getting `a`, we manually assign `a = nums[i]`.

# ### **Does It Affect Performance?**
# No, both methods have the same **time complexity (O(n²))**. The only difference is **readability**:

# | Approach            | Readability  | Explicit Control Over `i` |
# |---------------------|-------------|---------------------------|
# | `for i, a in enumerate(nums)` | ✅ More readable | ❌ Less explicit about `i` |
# | `for i in range(len(nums))` | ❌ Slightly less readable | ✅ More explicit about `i` |

# ### **Which One Should You Use?**
# - If you **don't** need `i` explicitly, `enumerate(nums)` is **cleaner**.
# - If you **need to modify `i`** or prefer explicit indexing, use `for i in range(len(nums))`.

# Both will work the same way, and it's mostly a **personal preference**. 🚀