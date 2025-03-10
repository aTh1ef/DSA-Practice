#neetcode 18
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        # loop to get the index of the target
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # to check if the left side is sorted
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:  # to check if the right side is sorted
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    answer = sol.search(nums, target)
    print(answer)

# Below is the **complete code** and a **line-by-line explanation** in simple, plain language. I'll also provide a **step-by-step** example so you can visualize exactly what's happening. Think of this like I'm explaining it to a total beginner who just wants the how and why without a bunch of fancy talk.

# ---

# ## The Code

# ```python
# class Solution:                                      # 1
#     def search(self, nums: List[int], target: int) -> int:  # 2
#         l, r = 0, len(nums) - 1                      # 3

#         while l <= r:                                # 4
#             mid = (l + r) // 2                       # 5

#             if target == nums[mid]:                  # 6
#                 return mid                           # 7

#             if nums[mid] >= nums[l]:                 # 8  (Left side is sorted)
#                 if target >= nums[l] and target < nums[mid]:  # 9
#                     r = mid - 1                      # 10
#                 else:
#                     l = mid + 1                      # 11
#             else:                                    # 12  (Right side is sorted)
#                 if target > nums[mid] and target <= nums[r]:  # 13
#                     l = mid + 1                      # 14
#                 else:
#                     r = mid - 1                      # 15

#         return -1                                    # 16
# ```

# ---

# ## Line-by-Line Breakdown

# ### Line 1
# ```python
# class Solution:
# ```
# - **What it does**: Defines a **class** named `Solution`.
# - **Layman's terms**: Think of a class like a **blueprint** that groups our function(s) together. We're basically saying, "Hey Python, here's a container for our solution."

# ### Line 2
# ```python
# def search(self, nums: List[int], target: int) -> int:
# ```
# - **What it does**: Inside the `Solution` class, we create a **function** called `search`.
# - It takes:
#   - `nums`: a **list** of integers (this is the rotated sorted array).
#   - `target`: the integer we want to find.
# - It **returns** an integer, which is the **index** where `target` is found, or `-1` if it's not in `nums`.

# ### Line 3
# ```python
# l, r = 0, len(nums) - 1
# ```
# - **What it does**: Sets two **pointers**:
#   - `l` = **left index**, starting at 0 (the first element in `nums`).
#   - `r` = **right index**, starting at `len(nums) - 1` (the last element in `nums`).
# - **Layman's terms**: We're telling Python: "We're going to look between the first and last elements of the list. `l` is the start, `r` is the end."

# ### Line 4
# ```python
# while l <= r:
# ```
# - **What it does**: Begins a **loop** that continues as long as the left index `l` hasn't gone past the right index `r`.
# - **Layman's terms**: We keep searching in the portion of the array from `l` to `r`. If `l` becomes bigger than `r`, it means we've exhausted all possible places where `target` could be.

# ### Line 5
# ```python
# mid = (l + r) // 2
# ```
# - **What it does**: Finds the **middle index** between `l` and `r`. The `// 2` is integer division (no decimals).
# - **Layman's terms**: Think of `mid` as the **midpoint** in our current search range. We check `nums[mid]` to see if that's the target or if we need to search to the left or right.

# ### Line 6
# ```python
# if target == nums[mid]:
# ```
# - **What it does**: Compares the middle element to the `target`.
# - **Layman's terms**: "Hey, is the middle element exactly the number we're looking for?"

# ### Line 7
# ```python
# return mid
# ```
# - **What it does**: If we found the target, we **immediately** return the index `mid`.
# - **Layman's terms**: "We found the target at this position, so we're done!"

# ### Line 8
# ```python
# if nums[mid] >= nums[l]:
# ```
# - **What it does**: Checks if the **left side** (from `l` to `mid`) is sorted.
#   - If the value at `mid` is **greater than or equal** to the value at `l`, it means everything between `l` and `mid` is in non-decreasing order.
# - **Layman's terms**: "Look at the left portion. If the middle number is bigger (or the same) as the leftmost number, that left portion is sorted nicely."

# ### Lines 9–11
# ```python
# if target >= nums[l] and target < nums[mid]:
#     r = mid - 1
# else:
#     l = mid + 1
# ```
# - **What it does**:
#   - **Line 9**: Checks if the `target` is between the leftmost value `nums[l]` and the middle value `nums[mid]`.
#   - If **yes**, then we **shrink** our search range to the left half by setting `r = mid - 1`.
#   - If **no**, it means the target must be in the right half, so we move `l` to `mid + 1`.
# - **Layman's terms**: "Since the left side is sorted, if our target fits in that sorted zone, we look there (`r = mid - 1`). Otherwise, we skip the left side and go right (`l = mid + 1`)."

# ### Lines 12–15
# ```python
# else:
#     if target > nums[mid] and target <= nums[r]:
#         l = mid + 1
#     else:
#         r = mid - 1
# ```
# - **What it does**:
#   - This `else` means the **left side isn't sorted**, so the **right side** (from `mid` to `r`) must be sorted.
#   - We check if the `target` is between `nums[mid]` and `nums[r]`.
#     - If **yes**, we move `l` to `mid + 1` (search the sorted right portion).
#     - If **no**, we move `r` to `mid - 1`.
# - **Layman's terms**: "If the left side wasn't sorted, then the right side must be. We see if the target fits in the right side's range. If it does, we search there by moving `l`. If it doesn't, we shrink from the right by moving `r`."

# ### Line 16
# ```python
# return -1
# ```
# - **What it does**: If the `while` loop ends, it means we never found the `target`. So we return `-1`.
# - **Layman's terms**: "We've tried all possibilities and didn't find the number. Tell the caller we didn't find it."

# ---

# ## Visualization with an Example

# Let's say our array is:
# ```
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
# ```
# This array is a **rotated sorted array** (it was originally `[0, 1, 2, 4, 5, 6, 7]` before rotation).

# 1. **Initial Setup**
#    - `l = 0` (pointing at 4)
#    - `r = 6` (pointing at 2)
#    - `res` is not explicitly used here, but we track the index with `mid`.

# 2. **First Iteration**
#    - `mid = (0 + 6) // 2 = 3`
#    - `nums[mid] = 7`
#    - Compare `target (0)` with `nums[mid] (7)` → not a match.
#    - Check if `nums[mid] >= nums[l]` → `7 >= 4`? Yes. So left side `[4, 5, 6, 7]` is sorted.
#    - Is `target (0)` >= `nums[l] (4)` and < `nums[mid] (7)`? No (0 is not >= 4).
#    - So we go `else` → `l = mid + 1 = 4`.

# 3. **Second Iteration**
#    - Now `l = 4`, `r = 6`.
#    - `mid = (4 + 6) // 2 = 5`.
#    - `nums[mid] = 1`.
#    - Compare `target (0)` with `nums[mid] (1)` → not a match.
#    - Check if `nums[mid] >= nums[l]` → `1 >= 0`? Wait, `nums[l]` is `nums[4]`, which is `0`. So yes, `1 >= 0`. The left side `[0, 1]` is sorted.
#    - Is `target (0)` >= `nums[l] (0)` and < `nums[mid] (1)`? Yes, `0 >= 0` and `0 < 1`.
#    - So we do `r = mid - 1 = 4`.

# 4. **Third Iteration**
#    - Now `l = 4`, `r = 4`.
#    - `mid = (4 + 4) // 2 = 4`.
#    - `nums[mid] = 0`.
#    - Compare `target (0)` with `nums[mid] (0)` → match!
#    - Return `mid`, which is `4`.

# The function returns `4`, meaning `nums[4]` is `0`, exactly what we wanted.

# ---

# ## Why This Works (in Super Layman Terms)

# - We're using a **binary search** approach. Instead of checking every element, we check the **middle** each time.
# - Because the array is **rotated**, either the left half or the right half will be sorted at any moment.
# - By checking which half is sorted, we can decide if the target lies in that half or not, and we **narrow down** the search accordingly.
# - This is way faster than scanning every element because we keep **cutting the search space in half**.

# ---

# ## Summary in Plain English

# 1. **Start** by looking at the whole array (from index 0 to the last index).
# 2. **Pick the middle** element. If it's the target, we're done!
# 3. **Otherwise**, check which side is sorted (left or right).
# 4. **If the left side is sorted**, see if our target fits there:
#    - If it does, we move our right boundary to `mid - 1`.
#    - If it doesn't, we move our left boundary to `mid + 1`.
# 5. **If the right side is sorted**, we do a similar check but reversed.
# 6. We keep doing this **until** we find the target or until `l` goes past `r`.
# 7. If we never find it, we return `-1`.

# That's it! We've gone **line by line**, explained each piece, and walked through an example. I hope this helps you **visualize** exactly how the code works in **super-layman** terms.

# ### Can we declare `mid = (l + r) // 2` **before** the `while` loop?

# Technically, you **can** write the line before the `while` loop...
# But it **won't work** the way you want.
# Here's **why**:

# ---

# ## Why It's Inside the Loop:
# ### `mid` depends on `l` and `r`.
# - `l` and `r` are **changing** as we search.
# - Every time we:
#   - Move `l` to `mid + 1`
#   - Or move `r` to `mid - 1`
# - We need to **recalculate** `mid`, because we're looking at a **new** portion of the array!

# ### If you calculate `mid` **only once**, before the loop:
# - It will **never update**, no matter how many times `l` and `r` change.
# - You'll just keep comparing the **same** middle index over and over…
# - And you'll likely end up in an **infinite loop** or get the wrong answer.

# ---

# ## Imagine It Like This (Visualization)

# ### Scenario 1: Correct way (inside the loop)
# - First time:
#   `l = 0`, `r = 6`, so `mid = 3`.
# - You update `l` or `r`. Let's say `l = mid + 1 = 4`.
# - Now you **recalculate**:
#   `mid = (4 + 6) // 2 = 5`.

# ### Scenario 2: Incorrect way (mid before the loop)
# - You calculate `mid = (0 + 6) // 2 = 3` once, and **never again**.
# - Even if `l` changes to 4, or `r` changes to 2,
#   `mid` stays stuck at 3!
# - Your comparisons are broken, and the loop doesn't work.

# ---

# ## Think of `mid` as Your **Scout**

# Imagine you're **searching** for treasure on an island:
# - You start by looking **in the middle** of the island.
# - If you don't find the treasure, you either search the **left side** or the **right side**.
# - But when you do that, you need to find the **middle of the new area** you're searching in!
# - If you kept using the **first middle point**, you'd never properly search the rest of the island.

# ---

# ## Code Snippet Showing What Happens:

# ### Wrong (outside loop - broken)
# ```python
# mid = (l + r) // 2  # calculated once
# while l <= r:
#     if target == nums[mid]:
#         return mid
#     # updates to l or r happen
#     # but mid never changes!
# ```

# ### Right (inside loop - works!)
# ```python
# while l <= r:
#     mid = (l + r) // 2  # recalculated every time l or r changes!
#     if target == nums[mid]:
#         return mid
#     # updates to l or r happen
# ```

# ---

# ## TL;DR:
# - `mid = (l + r) // 2` needs to be **inside** the loop because `l` and `r` keep **changing**.
# - `mid` is like a **pointer** to the middle of where we're searching **right now**—and "right now" keeps changing.
# - If you don't move the pointer, you're searching the same spot over and over.
# - Think of it like a GPS that needs to **recalculate** its route every time you turn!
