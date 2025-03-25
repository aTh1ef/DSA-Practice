#neetcode 37
class Solution(object):
    def canJump(self, nums):
        # Set the goal as the last index of the array
        goal = len(nums) - 1

        # Iterate through the array in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # If the current index plus its jump value reaches or exceeds the goal,
            # update the goal to the current index
            if i + nums[i] >= goal:
                goal = i

        # If the goal reaches index 0, return True (we can reach the last index)
        return goal == 0

# Let's visualize the **canJump** function using an example.

# ### Example:
# ```python
# nums = [2, 3, 1, 1, 4]
# ```
# This means:
# - From index `0`, you can jump up to `2` steps.
# - From index `1`, you can jump up to `3` steps.
# - From index `2`, you can jump up to `1` step.
# - From index `3`, you can jump up to `1` step.
# - From index `4`, you can jump up to `4` steps (which doesn't matter since it's the last index).

# ---

# ### Step-by-Step Visualization:
# We start from the last index (goal = `4`) and check if we can reach it from earlier indices.

# 1. **i = 4:**
#    - `i + nums[i] = 4 + 4 = 8` (greater than 4)
#    - We can already reach `4`, so goal remains `4`.

# 2. **i = 3:**
#    - `i + nums[i] = 3 + 1 = 4`
#    - Since `4 >= goal`, we update `goal = 3`.

# 3. **i = 2:**
#    - `i + nums[i] = 2 + 1 = 3`
#    - Since `3 >= goal`, we update `goal = 2`.

# 4. **i = 1:**
#    - `i + nums[i] = 1 + 3 = 4`
#    - Since `4 >= goal`, we update `goal = 1`.

# 5. **i = 0:**
#    - `i + nums[i] = 0 + 2 = 2`
#    - Since `2 >= goal`, we update `goal = 0`.

# Since `goal` is now `0`, we return **True**, meaning we **can jump** to the last index.

# ---

# ### Visual Representation:
# ```
# Index:  0   1   2   3   4
# Nums:   2   3   1   1   4
#         ▲   ▲   ▲   ▲   ▲
#         ↓   ↓   ↓   ↓   ↓
# Goal:   0 → 1 → 2 → 3 → 4
# ```
# Since we reduced the goal to `0`, we can reach the last index.