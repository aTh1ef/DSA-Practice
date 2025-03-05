#neetcode 9
class Solution():
    def validPalindrome(self, s):
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        return cleaned == cleaned[::-1]

if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    answer = sol.validPalindrome(s)
    print(answer)


# Let's break down the code into very simple, step-by-step explanations.
# Imagine you're new to programming—I'll explain it as simply as possible, line by line, with a little visualization too.
#
# ---
#
# ## The Code
#
# class Solution:
#     def isPalindrome(self, s):
#         cleaned = ""
#         for char in s:
#             if char.isalnum():
#                 cleaned += char.lower()
#         return cleaned == cleaned[::-1]
#
# ---
#
# ## What Does This Code Do?
#
# This function checks if a given string is a palindrome.
# A palindrome is a string that reads the same forward and backward (ignoring spaces, punctuation,
# and differences between uppercase and lowercase letters).
#
# ---
#
# ## Line-by-Line Explanation
#
# ### 1. `class Solution:`
# - **What it means:**
#   We create a class named `Solution`.
# - **Why:**
#   Many coding challenges (like on LeetCode) require you to put your solution inside a class.
#
# ---
#
# ### 2. `def isPalindrome(self, s):`
# - **What it means:**
#   This defines a function called `isPalindrome` inside the `Solution` class.
# - **What `s` is:**
#   It is the string you want to check.
# - **Why:**
#   The function will take this string, clean it up, and then determine if it’s a palindrome.
#
# ---
#
# ### 3. `cleaned = ""`
# - **What it does:**
#   It creates an empty string called `cleaned`.
# - **Why:**
#   We will build this string with only the characters we care about (letters and numbers) in lowercase.
# - **Visualization:**
#   Imagine starting with an empty basket where you’ll put in only the items (characters) you want.
#
# ---
#
# ### 4. `for char in s:`
# - **What it does:**
#   It goes through every character in the input string `s` one by one.
# - **Why:**
#   We need to check each character to see if it should be kept.
# - **Visualization:**
#   Think of it like reading the string letter by letter.
#
# ---
#
# ### 5. `if char.isalnum():`
# - **What it means:**
#   This line checks if the current character (`char`) is alphanumeric—that is, it’s a letter (like A–Z or a–z)
#   or a digit (0–9).
# - **Why:**
#   We only care about letters and numbers for checking palindromes.
#   Any punctuation, spaces, or symbols are ignored.
# - **Visualization:**
#   Imagine you have a filter that only allows letters and numbers into your basket.
#
# ---
#
# ### 6. `cleaned += char.lower()`
# - **What it does:**
#   If the character passes the check (it's alphanumeric), it is converted to lowercase using `char.lower()`
#   and then added to the end of the `cleaned` string.
# - **Why:**
#   Converting to lowercase ensures that uppercase and lowercase letters are treated the same (so "A" becomes "a").
# - **Visualization:**
#   Imagine every letter goes through a machine that makes it small (lowercase) before it’s added to your basket.
#
# ---
#
# ### 7. `return cleaned == cleaned[::-1]`
# - **What it does:**
#   This line compares the `cleaned` string with its reversed version.
# - **How it works:**
#   - `cleaned[::-1]` creates a new string that is the reverse of `cleaned`.
#   - For example, if `cleaned` is "abcba", then `cleaned[::-1]` is also "abcba".
# - **Why:**
#   If the original cleaned string is the same as its reverse, then it reads the same forward and backward,
#   which is exactly what a palindrome is.
# - **Visualization:**
#   Imagine writing the `cleaned` string on a piece of paper, then flipping the paper upside down (or reading it from the end)
#   to see if it spells the same word.
#
# ---
#
# ## Visual Example Walkthrough
#
# Let’s use the example:
# s = "A man, a plan, a canal: Panama"
#
# ### Step 1: Building the `cleaned` String
# - **Start with:** `cleaned = ""`
# - **Process each character:**
#   - 'A' is alphanumeric → convert to 'a' → `cleaned` becomes "a"
#   - ' ' (space) is ignored.
#   - 'm' is alphanumeric → already lowercase → add it → `cleaned` becomes "am"
#   - 'a' → add it → "ama"
#   - 'n' → add it → "aman"
#   - ',' (comma) is ignored.
#   - Continue this for every character...
# - **Result:**
#   After processing the entire string, `cleaned` becomes:
#   "amanaplanacanalpanama"
#
# ---
#
# ### Step 2: Checking if It's a Palindrome
# - **Reverse the `cleaned` string:**
#   "amanaplanacanalpanama"[::-1] also gives "amanaplanacanalpanama".
# - **Compare:**
#   Since "amanaplanacanalpanama" is equal to its reverse, the function returns True.
#
# ---
#
# ## Summary in Simple Terms
#
# 1. **Initialize an empty string** called `cleaned`.
# 2. **Go through every character** in your input string.
# 3. **For each character:**
#    - **If it's a letter or a number,** convert it to lowercase and add it to `cleaned`.
# 4. **Reverse the `cleaned` string.**
# 5. **Check if the cleaned string equals its reverse.**
#    - If they’re **equal**, return True (it’s a palindrome!).
#    - Otherwise, return False.
#
# This simple process helps you ignore spaces, punctuation, and letter case, so you can correctly decide whether the input is a palindrome.
#
# ---
#
# I hope this deep, detailed explanation makes everything super clear!