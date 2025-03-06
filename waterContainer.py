#neetcode 11
class Solution:
    def maxArea(self, height):
        result = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r-l) * min(height[l], height[r])
            result = max(result, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result

if __name__ == "__main__":
    height = [1,7,2,5,4,7,3,6]
    sol = Solution()
    answer = sol.maxArea(height)
    print(answer)

# Below is the **exact code** for the **Container With Most Water** problem using the **two-pointer (linear time)** approach, followed by a **line-by-line** explanation in very **plain, everyday language**. I'll try to be as detailed as possible, as if explaining to someone totally new to coding.

# ---

# ## The Code

# ```python
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         l, r = 0, len(height) - 1

#         while l < r:
#             area = (r - l) * min(height[l], height[r])
#             res = max(res, area)

#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1
#
#         return res
# ```

# ---

# ## Line-by-Line Breakdown

# ### 1. `class Solution:`
# - We're **defining a class** named `Solution`.
# - Many coding challenge platforms (like LeetCode) want your solution inside a class called `Solution`.

# ### 2. `def maxArea(self, height: List[int]) -> int:`
# - Inside the `Solution` class, we define a **method** called `maxArea`.
# - It takes one parameter, `height`, which is a list of integers.
# - The `-> int` part is just a **type hint** telling us this method will return an integer.

# ### 3. `res = 0`
# - We create a variable called `res` (short for "result") and **set it to 0**.
# - This will keep track of the **largest area** we find while checking different pairs of lines.

# ### 4. `l, r = 0, len(height) - 1`
# - We set up **two pointers**:
#   - `l` (**left pointer**) starts at the **first** index (`0`).
#   - `r` (**right pointer**) starts at the **last** index (`len(height) - 1`).
# - Think of it like we're looking at the **outermost** lines in the list first.

# ### 5. `while l < r:`
# - We start a **while loop** that runs as long as our left pointer is to the left of our right pointer (`l < r`).
# - We'll keep **moving these pointers** towards each other to find the maximum area.

# ### 6. `area = (r - l) * min(height[l], height[r])`
# - We calculate the **area** of water held between the line at index `l` and the line at index `r`.
# - The formula is:
#   - **Width** = `(r - l)`, which is the distance (horizontal) between the two lines.
#   - **Height** = `min(height[l], height[r])`, which is whichever of the two lines is **shorter** (because water will spill over the shorter line).
# - We multiply width by height to get the **area**.

# ### 7. `res = max(res, area)`
# - We update our **result** (`res`) if the newly calculated `area` is bigger than what we had before.
# - This way, `res` always holds the **largest area found so far**.

# ### 8. `if height[l] < height[r]:`
# - We check which line is **shorter**: the one at the left pointer (`height[l]`) or the one at the right pointer (`height[r]`).

# ### 9. `    l += 1`
# - If the **left line** is shorter, we **move the left pointer** to the right by 1 (`l += 1`).
# - Why? Because if the left line is the limiting factor (shorter line), we hope to find a **taller** line by moving the pointer inward.
# - This might help increase the `min(height[l], height[r])` part of our area calculation next time.

# ### 10. `else:`
# - If the above condition isn't true (meaning the right line is **shorter** or they're equal in height), we go to the `else` block.

# ### 11. `    r -= 1`
# - In the `else` block, we **move the right pointer** left by 1 (`r -= 1`).
# - Similar logic: if the right line is the limiting factor, we try to find a potentially **taller** line by moving inward from the right.

# ### 12. `return res`
# - After the `while l < r` loop finishes (meaning `l` has met or crossed `r`), we have tested all possible pairs in a **greedy, efficient** manner.
# - We **return** the maximum area found (`res`).

# ---

# ## Big-Picture Explanation

# Imagine you have a bunch of vertical lines of different heights. We want to hold as much water as possible between **two** of those lines. The **width** is how far apart they are, and the **height** is limited by the shorter line (water would spill over the top of the shorter line).

# 1. **Start Wide**: We pick the **leftmost** and **rightmost** lines first, giving us the maximum possible width.
# 2. **Move the Shorter Line**: Whichever line is shorter, we move that pointer inward to try and find a taller line that could increase our area.
# 3. **Keep Track of the Best**: Each time, we calculate the area and keep track of the **biggest** one.
# 4. **Repeat Until the Pointers Meet**: We keep doing this until the left pointer meets or crosses the right pointer.

# This **two-pointer** approach is **O(n)** because each pointer only moves inward up to `n` times in total. That's why it's often called the **linear** time solution.

# ---

# ## Visualizing a Quick Example

# Suppose our `height` list is: `[1, 8, 6, 2, 5, 4, 8, 3, 7]`.

# 1. **Left pointer** (`l`) starts at index `0` (height = 1).
# 2. **Right pointer** (`r`) starts at index `8` (height = 7).
# 3. Compute area:
#    - width = `8 - 0 = 8`
#    - height = `min(1, 7) = 1`
#    - area = `8 * 1 = 8`
#    - `res = max(0, 8) = 8`
# 4. Compare `height[l]` (1) vs. `height[r]` (7). The left line is shorter, so move `l` inward.
# 5. **Now `l=1` (height=8)**, `r=8` (height=7).
#    - width = `8 - 1 = 7`
#    - height = `min(8, 7) = 7`
#    - area = `7 * 7 = 49`
#    - `res = max(8, 49) = 49`
# 6. Compare `height[l]` (8) vs. `height[r]` (7). The right line is shorter, move `r` inward.
# 7. We keep going until `l` meets `r`, always updating the best `res`.

# By the end, we have the **largest** container area found in just one pass from the outside in.

# ---

# ## Why This Works

# - The key insight is that the **area** depends on both **width** and **height**.
# - The **width** is largest at the start (when `l=0` and `r=len(height)-1`).
# - We **only move the pointer** at the shorter line, because **moving the pointer at the taller line cannot yield a bigger minimum height**—you'd just lose width and gain no advantage in height.
# - This approach systematically tries all promising pairs without checking every single pair (which would be O(n²)).

# ---

# ### In the End

# - You get the maximum possible water area using a simple **while** loop and some **pointer arithmetic**.
# - This approach is both **elegant** and **fast**.

# That's it! This line-by-line explanation should help you visualize what's happening at each step. If anything is still unclear, just let me know, and I'll dive deeper.