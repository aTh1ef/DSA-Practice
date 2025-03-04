#neetcode #6

class Solution:

    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, encodedString):
        result = []
        i = 0

        while i < len(encodedString):
            j = i

            while encodedString[j] != "#":
                j += 1

            length = int(encodedString[i:j])
            i = j + 1

            decodedString = encodedString[i: i + length]

            result.append(decodedString)

            i = i + length
        return result


class Solution:
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s  # Append "length#string" for each string
        return result

    def decode(self, encodedString):
        result = []  # List to store decoded strings
        i = 0       # Pointer to traverse the encoded string
        while i < len(encodedString):
            j = i
            # Find the '#' which marks the end of the length info
            while encodedString[j] != "#":
                j += 1
            # The substring from i to j represents the length of the next string
            length = int(encodedString[i:j])
            i = j + 1  # Move pointer to the start of the actual string
            # Extract the string of the given length
            decodedString = encodedString[i : i + length]
            result.append(decodedString)
            i += length  # Move pointer to the start of the next encoded segment
        return result

if __name__ == "__main__":

    sol = Solution()


    strs = ["Hello", "World"]

    # Encode the list of strings
    encoded = sol.encode(strs)
    print("Encoded string:", encoded)

    # Decode the encoded string back into a list of strings
    decoded = sol.decode(encoded)
    print("Decoded list:", decoded)


# Below is a **very detailed, line-by-line explanation** of the **Encode and Decode Strings** solution (LeetCode 271).

# ---

# ## **Overall Idea**

# - **`encode(...)`** takes a list of strings (e.g. `["Hello", "World"]`) and **turns it into a single string**.
# - **`decode(...)`** takes that **single encoded string** and **splits it back** into the original list of strings.

# **Why do we need this?** Sometimes we need to store or send a list of strings in a format that we can **reliably decode** later (for example, storing them in a database or sending them over a network). We can't just join them with a simple delimiter like a comma, because what if the strings themselves contain commas?

# **This solution** solves that by **prefixing each string with its length**, plus a special marker (`#`), so we always know how many characters to read for each string.

# ---

# ## **Code (Typical Implementation)**

# Imagine we have a class called `Codec` with two methods: `encode` and `decode`.

# ```python
# class Codec:
#     def encode(self, strs):
#         """
#         Encodes a list of strings to a single string.
#         """
#         res = ""  # 1) Start with an empty string

#         for s in strs:  # 2) Loop through each string in the list
#             res += str(len(s)) + "#" + s  # 3) Append "length#string"

#         return res  # 4) Return the final encoded string

#     def decode(self, encoded_str):
#         """
#         Decodes a single string back into a list of strings.
#         """
#         res = []  # 5) This will hold our decoded strings
#         i = 0     # 6) We'll use i to keep track of our position in encoded_str

#         while i < len(encoded_str):  # 7) Loop until we've processed all characters
#             j = i
#             # 8) Find the '#' character to separate the length from the actual string
#             while encoded_str[j] != '#':
#                 j += 1

#             # 9) The part from i to j is the length of the next string
#             length = int(encoded_str[i:j])

#             # 10) Move past the '#' character
#             i = j + 1

#             # 11) Extract the substring of the specified length
#             decoded_string = encoded_str[i : i + length]
#             res.append(decoded_string)

#             # 12) Move i forward by 'length' to read the next string
#             i = i + length

#         return res
# ```

# ---

# ## **Step-by-Step Walkthrough**

# Let's pick an **example**:
# ```python
# strs = ["Hello", "World"]
# ```
# We'll see how `encode(strs)` produces a single string, and then how `decode(...)` turns it back into `["Hello", "World"]`.

# ### **A) Encoding**

# #### **Code**:
# ```python
# def encode(self, strs):
#     res = ""
#     for s in strs:
#         res += str(len(s)) + "#" + s
#     return res
# ```

# #### **Line-by-Line Explanation**:

# 1. **`res = ""`**
#    - We create an **empty string** `res` that will gradually hold our final result.
#    - Think of `res` as a container that we'll fill up.

# 2. **`for s in strs:`**
#    - We **loop through** each string in the list `strs`.
#    - For our example:
#      - First loop: `s = "Hello"`
#      - Second loop: `s = "World"`

# 3. **`res += str(len(s)) + "#" + s`**
#    - We take the **length** of the string `s`, convert it to a string with `str(len(s))`, then add a `#`, and then add the actual string `s`.
#    - **Why `str(len(s)) + "#" + s`?**
#      - This format says: "Here's how many characters to read, then a `#` to mark the end of the length, then the actual string."
#    - For `"Hello"` (which has length 5):
#      - `str(len("Hello"))` → `"5"`
#      - So we do: `res += "5#Hello"`
#      - Now `res = "5#Hello"`
#    - For `"World"` (which has length 5):
#      - `str(len("World"))` → `"5"`
#      - So we do: `res += "5#World"`
#      - Now `res = "5#Hello5#World"`

# 4. **`return res`**
#    - We return the **final encoded string**.
#    - In our example, **`res`** becomes `"5#Hello5#World"`.

# #### **Final Encoded Result**:
# ```python
# "5#Hello5#World"
# ```
# *(That's the entire list of strings collapsed into one string, with length markers.)*

# ---

# ### **B) Decoding**

# #### **Code**:
# ```python
# def decode(self, encoded_str):
#     res = []
#     i = 0
#     while i < len(encoded_str):
#         j = i
#         while encoded_str[j] != '#':
#             j += 1
#         length = int(encoded_str[i:j])
#         i = j + 1
#         decoded_string = encoded_str[i : i + length]
#         res.append(decoded_string)
#         i = i + length
#     return res
# ```

# #### **Line-by-Line Explanation**:

# 1. **`res = []`**
#    - We create an **empty list** to store our **decoded strings**.
#    - Think of `res` as a list that we'll fill up with each original string we extract.

# 2. **`i = 0`**
#    - This `i` is like a **pointer** or an **index** that will walk through the `encoded_str`.

# 3. **`while i < len(encoded_str):`**
#    - We loop until we've processed all characters in `encoded_str`.
#    - For our example, `encoded_str = "5#Hello5#World"`, which has length 13 characters.
#    - So, as long as `i` is less than 13, we keep going.

# 4. **`j = i`**
#    - We create another pointer `j` that will help us find the `#`.

# 5. **`while encoded_str[j] != '#': j += 1`**
#    - We move `j` forward until it finds the `#` character.
#    - **Why?** Because we know the substring between `i` and `j` is the length of our next string.
#    - For the first string:
#      - Initially, `i = 0`, `j = 0`.
#      - We move `j` until we see the `#`.
#      - The `#` is at position 1 in `"5#Hello5#World"`.
#      - So we stop when `j = 1`.

# 6. **`length = int(encoded_str[i:j])`**
#    - We **convert** the substring between `i` and `j` into an integer. This tells us how many characters we need to read for the string.
#    - First time: `encoded_str[0:1]` → `"5"`, `length = 5`.
#    - This means the next string is **5 characters long**.

# 7. **`i = j + 1`**
#    - We **move `i` past the `#`**.
#    - Now `i` points to the **start** of the actual string content.
#    - First time: `j = 1`, so `i = 1 + 1 = 2`.
#    - In `"5#Hello5#World"`, index 2 is where `"Hello"` starts.

# 8. **`decoded_string = encoded_str[i : i + length]`**
#    - We **extract** the substring of length `length` starting at `i`.
#    - First time: `i = 2`, `length = 5`, so `encoded_str[2 : 2 + 5] = encoded_str[2 : 7]`.
#    - That's `"Hello"`.

# 9. **`res.append(decoded_string)`**
#    - We add this decoded string to our `res` list.
#    - Now `res = ["Hello"]`.

# 10. **`i = i + length`**
#     - We move our pointer `i` forward by `length` so we can process the next string.
#     - First time: `i = 2 + 5 = 7`.
#     - Now `i` is at index 7, which is the start of `"5#World"`.

# 11. **Loop Repeats**
#     - We go back to **Step 3** as long as `i < len(encoded_str)`.
#     - Next iteration:
#       - `i = 7`, so we find the next `#`. That's at index 8.
#       - `length = int(encoded_str[7:8]) = 5`.
#       - Move `i` to `8 + 1 = 9`.
#       - Extract the next 5 characters: `encoded_str[9 : 14] → "World"`.
#       - Append `"World"` to `res`: `res = ["Hello", "World"]`.
#       - Move `i` by 5 → `i = 9 + 5 = 14`.
#       - Now `i = 14` which is `>= len(encoded_str)` (13). So we exit the loop.

# 12. **`return res`**
#     - Finally, we **return** the list of decoded strings.
#     - In our example, that's `["Hello", "World"]`.

# ---

# ## **Final Visualization**

# 1. **Encode**
#    - Input: `["Hello", "World"]`
#    - Output (single string): `"5#Hello5#World"`

# 2. **Decode**
#    - Input: `"5#Hello5#World"`
#    - Output (list of strings): `["Hello", "World"]`

# ---

# ## **Why This Works**
# - We **avoid** any confusion about special characters by **explicitly storing each string's length**.
# - The `#` acts like a **separator** between the length and the string itself.
# - During decoding, we **read the length** first, so we know **exactly how many characters** to grab for the next string.

# ---

# ## **Key Takeaways (In Plain English)**

# 1. **Storing the length** of each string solves the "where do I split?" problem.
# 2. We put **length + `#` + the string** in a row, repeated for all strings.
# 3. To **decode**, we just do the **reverse**:
#    - Read the number before `#` → that's how many characters to grab.
#    - Grab them → that's one original string.
#    - Keep doing this until we reach the end of the encoded string.

# ---

# ### **That's it!**
# You've got a straightforward way to **encode** a list of strings into one big string and **decode** it back. It's like packing items in boxes with **labels** telling you how big each item is. Then when you unpack, you read the label to know how big the item is, and you pull out exactly that many characters.
