# neetcode 75 - 4q

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    sol = Solution()
    answer = sol.groupAnagrams(strs)
    print(answer)

# Group Anagrams - Detailed Explanation
# =====================================

# PROBLEM:
# Given a list of strings, group anagrams together (words with same letters in different order)
# Example Input: ["act", "pots", "tops", "cat", "stop", "hat"]
# Example Output: [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

# SOLUTION APPROACH:
# We'll use a character frequency counter to identify anagrams instead of sorting

# IMPORTS:
# from typing import List - For type hints
# from collections import defaultdict - For automatic list creation with new keys

# ALGORITHM:
# 1. Create a defaultdict to store anagram groups
# 2. For each word:
#    a. Create a character frequency counter (26 zeros for a-z)
#    b. Count occurrences of each letter
#    c. Use this count as a key to group anagrams
# 3. Return all the grouped anagrams

# CODE WALKTHROUGH:

# Step 1: Import necessary modules
# - List for type annotations
# - defaultdict to avoid KeyError when inserting new words
# from typing import List
# from collections import defaultdict

# Step 2: Define the solution class and function
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         # Step 3: Create a dictionary to store anagram groups
#         # - Keys: tuples representing letter frequencies
#         # - Values: lists of words that are anagrams
#         res = defaultdict(list)

#         # Step 4: Process each word in the input list
#         for s in strs:

#             # Step 5: Create a character frequency counter
#             # - 26 zeros, one for each letter a-z
#             count = [0] * 26

#             # Step 6 & 7: Count frequency of each letter in the word
#             for c in s:
#                 # Convert character to index (0-25) and increment count
#                 # Example: 'a' -> 0, 'b' -> 1, etc.
#                 count[ord(c) - ord("a")] += 1

#             # Step 8: Use the frequency count as a key to group anagrams
#             # - Convert count to tuple (lists can't be dictionary keys)
#             # - Append current word to its anagram group
#             res[tuple(count)].append(s)

#         # Step 9: Return all the grouped anagrams
#         return res.values()

# EXAMPLE EXECUTION:
# For input ["act", "pots", "tops", "cat", "stop", "hat"]:
#
# Word: "act"
# - Count: [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] (1a, 1c, 1t)
# - Dictionary: {(1,0,1,...,1,...): ["act"]}
#
# Word: "pots"
# - Count: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0] (1o, 1p, 1s, 1t)
# - Dictionary: {(1,0,1,...): ["act"], (0,...,1,1,0,0,1,1,...): ["pots"]}
#
# Word: "tops"
# - Count: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0] (same as "pots")
# - Dictionary: {(1,0,1,...): ["act"], (0,...,1,1,0,0,1,1,...): ["pots", "tops"]}
#
# Word: "cat"
# - Count: [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] (same as "act")
# - Dictionary: {(1,0,1,...): ["act", "cat"], (0,...,1,1,0,0,1,1,...): ["pots", "tops"]}
#
# Word: "stop"
# - Count: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0] (same as "pots")
# - Dictionary: {(1,0,1,...): ["act", "cat"], (0,...,1,1,0,0,1,1,...): ["pots", "tops", "stop"]}
#
# Word: "hat"
# - Count: [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] (1a, 1h, 1t)
# - Dictionary: {(1,0,1,...): ["act", "cat"],
#                (0,...,1,1,0,0,1,1,...): ["pots", "tops", "stop"],
#                (1,0,0,...,1,...,1,...): ["hat"]}
#
# Final result: [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

# TIME COMPLEXITY: O(NK) where N is number of strings and K is max string length
# - We iterate through each string (N) and each character in the string (K)
# - This is more efficient than sorting each string O(NK log K)

# SPACE COMPLEXITY: O(NK) for storing all strings in the dictionary

# WHY THIS IS EFFICIENT:
# 1. Avoids sorting strings (which would be O(K log K) per string)
# 2. Uses character counting which is O(K) per string
# 3. Uses a dictionary for fast lookups and insertions
# 4. Only needs to iterate through each character once

# ## **Code Breakdown with Example Side by Side**

# ### **Example Input**
# ```python
# strs = ["act", "pots", "tops", "cat", "stop", "hat"]
# ```

# ---

# ### **Step 1: Import Required Modules**
# ```python
# from typing import List
# from collections import defaultdict
# ```
# ✅ **What happens?**
# - `defaultdict(list)` helps us store words in lists **without worrying about KeyErrors**.

# ---

# ### **Step 2: Define the Function**
# ```python
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# ```
# ✅ **What happens?**
# - We define a function that takes `strs` (a list of words) and returns **groups of anagrams**.

# ---

# ### **Step 3: Create a Dictionary to Store Anagrams**
# ```python
#         res = defaultdict(list)
# ```
# ✅ **What happens?**
# - Creates an **empty dictionary** to store anagram groups.

# 📌 **Dictionary state:**
# ```python
# res = {}
# ```

# ---

# ### **Step 4: Loop Through Each Word**
# ```python
#         for s in strs:
# ```
# ✅ **What happens?**
# - We **iterate through each word** in `strs`.

# 📌 **First word: `"act"`**
# 📌 **Second word: `"pots"`**
# 📌 **Third word: `"tops"`**
# 📌 **Fourth word: `"cat"`**
# 📌 **Fifth word: `"stop"`**
# 📌 **Sixth word: `"hat"`**

# ---

# ### **Step 5: Create a Character Frequency List**
# ```python
#             count = [0] * 26
# ```
# ✅ **What happens?**
# - We make a **list of 26 zeros** (one for each letter 'a' to 'z').

# 📌 **Before Processing "act"**
# ```python
# count = [0, 0, 0, 0, ..., 0]  # 26 zeros
# ```

# ---

# ### **Step 6: Loop Through Each Letter in the Word**
# ```python
#             for c in s:
# ```
# ✅ **What happens?**
# - We **loop through each letter** of the current word.

# 📌 **Processing "act"**
# - `'a'` → `count[0] += 1`
# - `'c'` → `count[2] += 1`
# - `'t'` → `count[19] += 1`

# 📌 **Final `count` for "act"**
# ```python
# count = [1, 0, 1, 0, 0, ..., 0, 1, 0, 0, 0]
# ```
# (Only 'a', 'c', and 't' positions changed)

# ---

# ### **Step 7: Store the Word in the Dictionary**
# ```python
#             res[tuple(count)].append(s)
# ```
# ✅ **What happens?**
# - Convert `count` into a **tuple** and use it as a **key** in `res`.
# - **Append "act"** under this key.

# 📌 **Dictionary after "act"**
# ```python
# res = {
#     (1,0,1,0,...,1,0,0,0,0,0): ["act"]
# }
# ```

# ---

# ### **Repeat Steps 5-7 for Each Word**
# #### **Processing "pots"**
# - `'p'` → `count[15] += 1`
# - `'o'` → `count[14] += 1`
# - `'t'` → `count[19] += 1`
# - `'s'` → `count[18] += 1`

# 📌 **Final `count` for "pots"**
# ```python
# count = [0,0,0,0,0,...,1,1,1,1,0,0,0]
# ```

# 📌 **Dictionary after "pots"**
# ```python
# res = {
#     (1,0,1,0,...,1,0,0,0,0,0): ["act"],
#     (0,0,0,0,...,1,1,1,1,0,0,0): ["pots"]
# }
# ```

# ---

# #### **Processing "tops"**
# 📌 `"tops"` has the **same letter frequencies** as `"pots"`.

# ✅ `"tops"` goes into the **same group** as `"pots"`.

# 📌 **Dictionary after "tops"**
# ```python
# res = {
#     (1,0,1,0,...,1,0,0,0,0,0): ["act"],
#     (0,0,0,0,...,1,1,1,1,0,0,0): ["pots", "tops"]
# }
# ```

# ---

# #### **Processing "cat"**
# 📌 `"cat"` has the **same letter frequencies** as `"act"`.

# ✅ `"cat"` goes into the **same group** as `"act"`.

# 📌 **Dictionary after "cat"**
# ```python
# res = {
#     (1,0,1,0,...,1,0,0,0,0,0): ["act", "cat"],
#     (0,0,0,0,...,1,1,1,1,0,0,0): ["pots", "tops"]
# }
# ```

# ---

# #### **Processing "stop"**
# 📌 `"stop"` has the **same letter frequencies** as `"pots" and "tops"`.

# ✅ `"stop"` goes into the **same group**.

# 📌 **Dictionary after "stop"**
# ```python
# res = {
#     (1,0,1,0,...,1,0,0,0,0,0): ["act", "cat"],
#     (0,0,0,0,...,1,1,1,1,0,0,0): ["pots", "tops", "stop"]
# }
# ```

# ---

# #### **Processing "hat"**
# 📌 `"hat"` has a **new character frequency**.

# ✅ `"hat"` starts a **new group**.

# 📌 **Final Dictionary**
# ```python
# res = {
#     (1,0,1,0,...,1,0,0,0,0,0): ["act", "cat"],
#     (0,0,0,0,...,1,1,1,1,0,0,0): ["pots", "tops", "stop"],
#     (0,1,1,0,...,0,1,0,0,0): ["hat"]
# }
# ```

# ---

# ### **Step 8: Return the Groups of Anagrams**
# ```python
#         return res.values()
# ```
# ✅ **What happens?**
# - `res.values()` returns all **lists of grouped anagrams**.

# 📌 **Final Output**
# ```python
# [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
# ```

# ---

# ## **Final Output**
# ```python
# [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
# ```

# ---

# ## **🚀 Why This is Optimal**
# - ✅ **Avoids Sorting**: Sorting is **O(K log K)**, but counting letters is **O(K)**.
# - ✅ **Uses a Dictionary**: Fast **O(1)** lookups and insertions.
# - ✅ **Time Complexity**: **O(NK)** (where **N** = number of words, **K** = max word length).
# - ✅ **Space Complexity**: **O(NK)** (since we store words in a dictionary).

# ---

# ## **🔥 TL;DR (Too Long, Didn't Read)**
# 1. **Convert each word into a letter frequency tuple**.
# 2. **Use this tuple as a dictionary key**.
# 3. **Group words with the same key together**.
# 4. **Return grouped anagrams**.