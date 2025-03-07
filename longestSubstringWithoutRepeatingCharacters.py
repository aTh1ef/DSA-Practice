#neetccode #13

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result

if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    answer = sol.lengthOfLongestSubstring(s)
    print(answer)


# Below is **every single line** of the program, followed by a **super-simple, "explain it like I'm a total newbie (or 'dumbass')"** breakdown. I'll also include a simple **visual** idea to help you really see what's going on. Ready? Let's go line by line.

# ---

# ## The Code (All Lines Shown)

# ```python
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)

#         return res
# ```

# ---

# ## Line-by-Line Explanation (In Very Simple Terms)

# ### 1. `class Solution:`
# - **What it does:** We're creating a "blueprint" (a class) called **Solution**.
# - **Why it matters:** In many coding platforms (like LeetCode), you wrap your solution in a class. That's just how they expect the code to be organized.

# ### 2. `def lengthOfLongestSubstring(self, s: str) -> int:`
# - **What it does:** We define a **function** named `lengthOfLongestSubstring`. It takes an input string `s` and will **return** an integer (`-> int`).
# - **Why it matters:** This function is the main workhorse. It's where we do all the logic to find the longest substring without repeating characters.

# ### 3. `charSet = set()`
# - **What it does:** We create an empty **set** called `charSet`. A **set** in Python is like a box that automatically makes sure it doesn't keep duplicates.
# - **Why it matters:** We will use this set to keep track of which characters are currently in our "window" (the substring we're checking). If a character is in this set, it means we already have it in our current substring.

# ### 4. `l = 0`
# - **What it does:** We set a variable `l` (short for "left") to **0**.
# - **Why it matters:** We'll use `l` to mark the **left boundary** of our sliding window. Picture we have two pointers: `l` (left) and `r` (right). They define the section of the string we're currently considering.

# ### 5. `res = 0`
# - **What it does:** We set a variable `res` (short for "result") to **0**.
# - **Why it matters:** We'll keep track of the **maximum length** we find for a substring without repeating characters. Initially, it's 0 because we haven't started checking yet.

# ### 6. `for r in range(len(s)):`
# - **What it does:** We start a **for loop** that goes from `r = 0` up to `r = len(s)-1`.
# - **Why it matters:** `r` (short for "right") will be the **right boundary** of our sliding window. As `r` moves forward through the string, we'll check characters one by one.

# ### 7. `while s[r] in charSet:`
# - **What it does:** This line says: **"As long as the character at position `r` is already in our set, do something."**
# - **Why it matters:** If `s[r]` is already in `charSet`, it means we have a **repeat** in our current window. We can't have that if we want a substring with **no** repeating characters. So we'll need to move the left side (`l`) to remove that duplicate from the window.

# ### 8. `charSet.remove(s[l])`
# - **What it does:** We remove the character at the **left** pointer `l` from the set.
# - **Why it matters:** By removing `s[l]` from the set, we're basically **shrinking** the window from the left side. We're trying to get rid of the old character so that we can eventually add `s[r]` (the new character) without any duplicates.

# ### 9. `l += 1`
# - **What it does:** We move the left pointer `l` one step to the right.
# - **Why it matters:** We just removed the character at `l`, so we need to **advance** `l` by 1. Now our window starts at the new `l`.

# > **Note:** Steps 7, 8, and 9 happen in a loop (`while`) because there might be multiple duplicates if we don't keep moving `l` until the new character `s[r]` is no longer a duplicate in the set.

# ### 10. `charSet.add(s[r])`
# - **What it does:** After making sure `s[r]` is **not** in the set (by removing any duplicates we had), we now add `s[r]` to the set.
# - **Why it matters:** We're extending our window to include the new character at position `r`. Now the set has all the unique characters in our current window.

# ### 11. `res = max(res, r - l + 1)`
# - **What it does:** We calculate the **length** of the current window (`r - l + 1`) and see if it's bigger than our current `res`. If it's bigger, we update `res`.
# - **Why it matters:** This is how we keep track of the **longest** window (substring) without repeating characters that we've found so far.

# ### 12. `return res`
# - **What it does:** After the loop finishes (we've moved `r` all the way through the string), we **return** the result `res`.
# - **Why it matters:** This is the final answer: the **length** of the longest substring without repeating characters.

# ---

# ## How to Visualize It (A Simple Mental Picture)

# 1. **Imagine** you have a **sliding window** that starts with left = 0 and right = 0.
# 2. As you move `right` through the string:
#    - If the character at `right` is **not** in the set, we add it and update our result length if needed.
#    - If the character at `right` **is** already in the set, we start **kicking out** characters from the left side until that character is removed.
# 3. This way, the window always contains **unique characters**.
# 4. We keep track of the **maximum size** that window ever reaches.

# **Example** (with the string `"abcabcbb"`):
# - Start with `l = 0`, `r = 0`, `charSet = {}`, `res = 0`.
# - `r = 0` → character is `'a'`. `'a'` not in set, so add `'a'`. Now set = `{ 'a' }`, window size = `r - l + 1 = 1`. `res = max(0, 1) = 1`.
# - `r = 1` → `'b'`. Not in set, add `'b'`. Now set = `{ 'a', 'b' }`, window size = 2. `res = 2`.
# - `r = 2` → `'c'`. Not in set, add `'c'`. set = `{ 'a', 'b', 'c' }`, window size = 3. `res = 3`.
# - `r = 3` → `'a'`. **But** `'a'` is **in** set, so remove the left character (`'a'` at index 0). Now set = `{ 'b', 'c' }`. Then move `l` to `1`. Now `'a'` is **not** in the set, we can add `'a'`. The window is now from `l = 1` to `r = 3`, set = `{ 'b', 'c', 'a' }`, window size = 3, `res = max(3, 3) = 3`.
# - … and so on, until `r` reaches the end of the string.

# By the end, `res` holds the largest window size we found, which for `"abcabcbb"` is **3** (the substring `"abc"` or `"bca"`, etc.).

# ---

# ## Putting It All Together

# - **We use a set** to quickly check if we've seen a character already in our current window.
# - **We use two pointers**, `l` and `r`, to represent the **start** and **end** of our window.
# - **Whenever** we see a duplicate, we **slide** the left pointer until the duplicate is gone.
# - We **update** our answer with the **maximum** window size found along the way.
# - We **return** that maximum window size.

# ---

# ### Final Thoughts

# This approach is known as the **sliding window** technique, and it runs in **O(n)** time for a string of length **n**, because:
# - Each character is visited **at most twice** (once when `r` moves right, and possibly once when `l` moves up).
# - Checking membership in a **set** and adding/removing from it is typically **O(1)**.

# That's it! Hopefully, this breakdown is clear enough that **anyone** can follow it—no matter how "not so smart" they think they are. You got this!
