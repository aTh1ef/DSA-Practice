#neetcode 14

class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        result = 0
        maxf = 0
        l = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        return result

if __name__ == "__main__":
    sol = Solution()
    s = "XYYX"
    k = 2
    answer = sol.characterReplacement(s, k)
    print(answer)

# Below is the entire rewritten code with detailed, line-by-line explanations in simple, layman's language. I'll explain every part and even walk you through a visual example so it's super clear.

# ---

# ```python
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         # Create an empty dictionary to count how many times each character appears
#         count = {}
#
#         # 'res' will hold the length of the longest substring we can achieve
#         res = 0
#
#         # 'l' (left pointer) marks the beginning of our sliding window
#         l = 0
#
#         # 'maxf' keeps track of the highest count (frequency) of any one character in the current window
#         maxf = 0

#         # 'r' (right pointer) will move from the beginning to the end of the string 's'
#         for r in range(len(s)):
#             # --- Update the count dictionary for the character at the right pointer ---
#             # If the character s[r] is already in the dictionary, add 1 to its count.
#             # Otherwise, if it's not there yet, start its count at 1.
#             if s[r] in count:
#                 count[s[r]] += 1
#             else:
#                 count[s[r]] = 1

#             # --- Update 'maxf' ---
#             # Check if the new count for s[r] is higher than our current max frequency in the window.
#             maxf = max(maxf, count[s[r]])

#             # --- Check if the current window is valid ---
#             # (r - l + 1) is the length of the current window.
#             # If (window length - maxf) is more than k, it means we need to change more than k characters
#             # to make all characters in the window the same.
#             while (r - l + 1) - maxf > k:
#                 # We remove the character at the left pointer from our window.
#                 # So, decrease its count since it is no longer in the current window.
#                 count[s[l]] -= 1
#                 # Move the left pointer to the right to shrink the window.
#                 l += 1

#             # --- Update the result ---
#             # After adjusting the window (if needed), check if the current window size is the largest valid one.
#             res = max(res, r - l + 1)

#         # Return the maximum window size found which is our answer.
#         return res
# ```

# ---

# ### Detailed Explanation (Line by Line)

# 1. **`class Solution:`**
#    - **What it means:** This defines a new class called `Solution`.
#    - **Simple terms:** Think of it as a box where our function lives. Many coding challenge sites require you to put your code in a class.

# 2. **`def characterReplacement(self, s: str, k: int) -> int:`**
#    - **What it means:** This line defines a function called `characterReplacement` inside the class. It accepts:
#      - A string `s` (the input text)
#      - An integer `k` (the maximum number of characters you're allowed to change)
#    - **Simple terms:** This is our main function. You give it a string and a number, and it will return a number (the length of the longest substring you can get after at most `k` changes).

# 3. **`count = {}`**
#    - **What it means:** Initializes an empty dictionary that will keep track of how many times each character appears in our current window (a part of the string).
#    - **Simple terms:** Imagine you have a tally chart for the characters you see. It starts empty.

# 4. **`res = 0`**
#    - **What it means:** Creates a variable `res` to store the length of the best (longest) valid substring found so far.
#    - **Simple terms:** This is like keeping a high score for the best window we can create.

# 5. **`l = 0`**
#    - **What it means:** Sets the left pointer (`l`) at position 0.
#    - **Simple terms:** Picture a window on your string. `l` tells you where the window starts. Initially, it starts at the very beginning.

# 6. **`maxf = 0`**
#    - **What it means:** Sets `maxf` (maximum frequency) to 0.
#    - **Simple terms:** This keeps track of how many times the most common character appears in your current window. It starts at 0 because you haven't seen any characters yet.

# 7. **`for r in range(len(s)):`**
#    - **What it means:** Start a loop with `r` as the right pointer, which goes from the beginning to the end of the string.
#    - **Simple terms:** Now we slide the right side of our window across the string, one character at a time.

# 8. **Inside the loop – Updating the count:**
#    - **Code:**
#      ```python
#      if s[r] in count:
#          count[s[r]] += 1
#      else:
#          count[s[r]] = 1
#      ```
#    - **What it means:**
#      - Check if the current character `s[r]` is already in our tally (dictionary).
#      - If it is, add 1 to its count.
#      - If not, set its count to 1.
#    - **Simple terms:** You're saying, "I see this character now! If I already saw it, increase its tally; if not, start its count at 1."

# 9. **Updating `maxf`:**
#    - **Code:**
#      ```python
#      maxf = max(maxf, count[s[r]])
#      ```
#    - **What it means:**
#      - Compare the current maximum frequency (`maxf`) with the updated count of the current character.
#      - Set `maxf` to the higher value.
#    - **Simple terms:** This line keeps track of the "top score" for the number of times any one character appears in our current window. If the new character makes the count higher, update it.

# 10. **Checking if the window is valid:**
#     - **Code:**
#       ```python
#       while (r - l + 1) - maxf > k:
#       ```
#     - **What it means:**
#       - `(r - l + 1)` calculates the size (length) of the current window.
#       - Subtracting `maxf` from the window size tells us how many characters in the window are *not* the most frequent.
#       - If this number is greater than `k`, it means we'd need to change more than `k` characters to make the window all the same, so the window is invalid.
#     - **Simple terms:** Imagine you want every letter in your window to be the same. The number of letters you'd need to change is `(window size - most frequent count)`. If that's more than what you're allowed (`k`), the window is too big, and you need to shrink it.

# 11. **Shrinking the window (inside the while loop):**
#     - **Code:**
#       ```python
#       count[s[l]] -= 1
#       l += 1
#       ```
#     - **What it means:**
#       - Remove the character at the left pointer from your count by subtracting 1.
#       - Move the left pointer to the right (increase `l` by 1) to shrink the window.
#     - **Simple terms:** Since the window is too big, we remove the leftmost character from our window and update our counts. It's like sliding the window's start one step to the right.

# 12. **Updating the result:**
#     - **Code:**
#       ```python
#       res = max(res, r - l + 1)
#       ```
#     - **What it means:**
#       - After possibly shrinking the window, compare the current window size (`r - l + 1`) with the best size (`res`) found so far.
#       - Store the larger value in `res`.
#     - **Simple terms:** Every time we adjust the window, we check if it's the biggest valid window we've seen. If yes, we remember that size.

# 13. **Returning the final result:**
#     - **Code:**
#       ```python
#       return res
#       ```
#     - **What it means:**
#       - Once the loop finishes, return `res` which holds the length of the longest substring that can be made all the same with at most `k` changes.
#     - **Simple terms:** After going through the entire string, give back the best answer (the largest window size).

# ---

# ### Visualization Example

# Imagine your string is `"AABABBA"` and you are allowed to change at most `k = 1` character.

# 1. **Start:**
#    - **Window:** `"A"`
#    - **Count:** `{'A': 1}`
#    - **maxf:** 1 (one A)
#    - **Needed changes:** `(window length 1 - 1) = 0` (0 ≤ 1, so valid)

# 2. **Expand to `"AA"`:**
#    - **Window:** `"AA"`
#    - **Count:** `{'A': 2}`
#    - **maxf:** 2
#    - **Needed changes:** `(2 - 2) = 0` (still valid)

# 3. **Expand to `"AAB"`:**
#    - **Window:** `"AAB"`
#    - **Count:** `{'A': 2, 'B': 1}`
#    - **maxf:** 2 (A still most common)
#    - **Needed changes:** `(3 - 2) = 1` (1 equals k, so still valid)

# 4. **Expand to `"AABA"`:**
#    - **Window:** `"AABA"`
#    - **Count:** `{'A': 3, 'B': 1}`
#    - **maxf:** 3
#    - **Needed changes:** `(4 - 3) = 1` (valid)

# 5. **Expand to `"AABAB"`:**
#    - **Window:** `"AABAB"`
#    - **Count:** `{'A': 3, 'B': 2}`
#    - **maxf:** 3
#    - **Needed changes:** `(5 - 3) = 2` (2 > 1, so invalid)
#    - **Action:** Shrink the window by moving `l` to the right until the needed changes become ≤ 1.

# 6. **Shrink Process:**
#    - Remove the leftmost character and update counts, then check if the window is valid again.
#    - The process continues until you have a valid window and then you update `res` if the window is the biggest found.

# At the end, `res` will be the length of the largest window where you can change at most 1 character to make all characters the same.

# ---

# ### Final Takeaway

# - **Sliding Window Technique:**
#   You keep a "window" (a part of the string) and slide it along, expanding when possible and shrinking when necessary.
# - **Counting Characters:**
#   A dictionary (`count`) tracks how many times each character appears.
# - **Most Frequent Character (`maxf`):**
#   Helps decide if the window can be made uniform with ≤ `k` changes.
# - **Result (`res`):**
#   Updated each time with the largest valid window size.

# This detailed, step-by-step explanation should help you visualize and understand exactly how each line works in the code. Let me know if you have any more questions or if any part needs further clarification!