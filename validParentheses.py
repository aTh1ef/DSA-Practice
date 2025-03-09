#neetcode 16

class Solution(object):
    def isValid(self, s):

        #First initialise a stack and a hashmap to get the optimal solution
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}

        #Next we run a loop. The loop will basically decide to add and pop the characters from the stack
        for i in range(len(s)):
            c = s[i]
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: #This condition here checks if the stack is not empty so that is why we write if stack and in python stack[-1] indicates the top of the stack so we check if the current element at the top of the stack matches to the closing parenthesis in the hashmap we created
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

if __name__ == "__main__":
    sol = Solution()
    s = "([{}])"
    answer = sol.isValid(s)
    print(answer)


# Below is the **complete code**, written **line by line**, followed by a **detailed, plain-English (layman's) explanation** for each line. Think of it like a step-by-step breakdown that assumes you're brand-new to programming and want every little detail. I'll also include a simple visualization of what's happening with the **stack** as we process each character.

# ---

# ## The Code

# ```python
# class Solution:                        # 1
#     def isValid(self, s: str) -> bool: # 2
#         stack = []                     # 3
#         closeToOpen = {")": "(", "]": "[", "}": "{"}  # 4

#         for i in range(len(s)):        # 5
#             c = s[i]                   # 6
#             if c in closeToOpen:       # 7
#                 if stack and stack[-1] == closeToOpen[c]:  # 8
#                     stack.pop()        # 9
#                 else:                  # 10
#                     return False       # 11
#             else:                      # 12
#                 stack.append(c)        # 13

#         return len(stack) == 0         # 14
# ```

# ---

# ## Line-by-Line Explanation

# ### Line 1
# ```python
# class Solution:
# ```
# - **What it does**: Defines a **class** named `Solution`.
# - **Layman's terms**: Think of a class like a **blueprint** for creating something (in this case, it's a blueprint for a solution that will hold our function).

# ### Line 2
# ```python
# def isValid(self, s: str) -> bool:
# ```
# - **What it does**: Inside the `Solution` class, we define a **function** (also called a **method** because it's inside a class) named `isValid`.
# - It takes two parameters:
#   - `self`: This is how Python refers to the current object of the class (standard for all class methods).
#   - `s: str`: This means `s` should be a string. The function is supposed to return a boolean (`True` or `False`).
# - **Layman's terms**: This is a function that checks if a string `s` has valid parentheses/brackets. It returns **True** if everything matches up nicely, or **False** if there's any mismatch.

# ### Line 3
# ```python
# stack = []
# ```
# - **What it does**: Creates an **empty list** named `stack`.
# - **Layman's terms**: Think of a **stack** like a stack of plates. You can only put a new plate on top or take the top plate off. We use this structure to keep track of opening brackets as we move through the string.

# ### Line 4
# ```python
# closeToOpen = {")": "(", "]": "[", "}": "{"}
# ```
# - **What it does**: Creates a **dictionary** that maps **closing brackets** to their corresponding **opening brackets**.
#   - `")"` maps to `"("`
#   - `"]"` maps to `"["`
#   - `"}"` maps to `"{"`
# - **Layman's terms**: If you see a `)`, it should match a `(`. If you see a `]`, it should match a `[`, and if you see a `}`, it should match a `{`. This dictionary helps us quickly check which opening bracket pairs with the closing one.

# ### Line 5
# ```python
# for i in range(len(s)):
# ```
# - **What it does**: Starts a **for loop** that will go through each **index** from `0` up to `len(s) - 1`.
# - **Layman's terms**: We want to examine every single character in the string `s`. This loop makes `i` go from 0 (the first character) to the last character's position in the string.

# ### Line 6
# ```python
# c = s[i]
# ```
# - **What it does**: Gets the character at index `i` from the string `s` and stores it in `c`.
# - **Layman's terms**: We're looking at the string one character at a time. For example, if `s = "([{}])"`, when `i = 0`, `c = '('`; when `i = 1`, `c = '['`; and so on.

# ### Line 7
# ```python
# if c in closeToOpen:
# ```
# - **What it does**: Checks if the current character `c` is **one of the closing brackets** (`)`, `]`, or `}`).
# - **Layman's terms**: We ask, "Is the character I'm looking at a **closing** bracket?" If **yes**, we handle it in a certain way; if **no**, that means it's an **opening** bracket (like `(`, `[`, or `{`).

# ### Line 8
# ```python
# if stack and stack[-1] == closeToOpen[c]:
# ```
# - **What it does**:
#   1. `if stack` checks if the stack is **not empty** (because if it's empty, we can't compare the top element).
#   2. `stack[-1]` means the **top element** of the stack (the last item in the list).
#   3. `== closeToOpen[c]` means we check if the top of the stack is the **matching opening bracket** for our current closing bracket `c`.
# - **Layman's terms**:
#   - First, we see if we even have any opening bracket stored in the stack.
#   - Then, we check if the top bracket on the stack is the correct matching partner. For example, if `c` is `)`, then `closeToOpen[c]` is `(`. We see if the top of the stack is indeed `(`.
#   - If yes, great—we have a match.

# ### Line 9
# ```python
# stack.pop()
# ```
# - **What it does**: Removes the **top element** (the last item) from the stack.
# - **Layman's terms**: If we found a matching pair (like `(` on the stack and `)` in our string), we **pop** the `(` off the stack, because that pair is now matched and complete. It's like removing the top plate from the stack once you've used it.

# ### Line 10
# ```python
# else:
# ```
# - **What it does**: This `else` goes with the `if stack and stack[-1] == closeToOpen[c]:` condition. It means if that condition is **not** true, we do what's in this `else` block.
# - **Layman's terms**: If the top of the stack **doesn't** match the closing bracket, or if the stack is empty when we see a closing bracket, we're in trouble—this means the parentheses are not valid.

# ### Line 11
# ```python
# return False
# ```
# - **What it does**: Immediately **exits** the function and returns `False`.
# - **Layman's terms**: If we get here, it means the string is **invalid** because the closing bracket does not have the correct matching opening bracket (or no opening bracket at all).

# ### Line 12
# ```python
# else:
# ```
# - **What it does**: This `else` pairs with the original `if c in closeToOpen:` (Line 7). If `c` **is not** in `closeToOpen`, that means `c` is an **opening bracket**.
# - **Layman's terms**: We do something different when `c` is an opening bracket (like `(`, `[`, or `{`).

# ### Line 13
# ```python
# stack.append(c)
# ```
# - **What it does**: Adds the current character `c` (an opening bracket) to the **top** of the stack (the end of the list).
# - **Layman's terms**: If it's an opening bracket, we put it on the stack, waiting to see if it will be matched by a future closing bracket. Think: we place a new plate on top of the stack.

# ### Line 14
# ```python
# return len(stack) == 0
# ```
# - **What it does**: After we finish the loop (meaning we've processed every character in `s`), we check if the **stack is empty**.
#   - `len(stack) == 0` is `True` if the stack has no items left.
# - **Layman's terms**:
#   - If the stack is empty, it means **every opening bracket** we put on the stack has found a matching closing bracket and was popped off. So the string is **valid**.
#   - If the stack is **not** empty, it means there are some unmatched opening brackets left, so the string is **invalid** (but we only return `True` if it's empty).

# ---

# ## Visualizing the Stack

# Let's visualize how the stack changes as we process a string.
# **Example**: `s = "({[]})"`

# 1. **Start**: `stack = []` (empty)
# 2. See `(` (opening bracket)
#    - `stack = ["("]`
# 3. See `{` (opening bracket)
#    - `stack = ["(", "{"]`
# 4. See `[` (opening bracket)
#    - `stack = ["(", "{", "["]`
# 5. See `]` (closing bracket)
#    - Check top of stack: it's `[`. The matching pair for `]` is `[`.
#    - Pop `[`.
#    - `stack = ["(", "{"]`
# 6. See `}` (closing bracket)
#    - Check top of stack: it's `{`. The matching pair for `}` is `{`.
#    - Pop `{`.
#    - `stack = ["("]`
# 7. See `)` (closing bracket)
#    - Check top of stack: it's `(`. The matching pair for `)` is `(`.
#    - Pop `(`.
#    - `stack = []`
# 8. End of string. `stack` is empty, so **return `True`**.

# If at any point we see a closing bracket that doesn't match the top of the stack, we **return `False`** right away. Also, if we finish processing all characters and still have leftover items in `stack`, we return `False`.

# ---

# ## Why This Works

# - The **stack** approach is a classic method for checking balanced parentheses/brackets.
# - Every time we see an **opening bracket**, we **push** (append) it onto the stack.
# - Every time we see a **closing bracket**, we check if it matches the **last opening bracket**. If it does, we pop that opening bracket off the stack. If not, the string is invalid.
# - If we finish and the stack is **empty**, all brackets matched up. If it's **not empty**, something didn't get matched.

# ---

# ## Summary in Super-Layman Terms

# - We read each character in the string, one by one.
# - If it's an **opening bracket** (`(`, `[`, or `{`), we **push it** onto the stack (like putting a plate on a pile).
# - If it's a **closing bracket** (`)`, `]`, or `}`), we see if it can match (pair up with) the top opening bracket on the stack. If it does match, we **pop** the top bracket off. If it doesn't match or there's nothing on the stack, we say "Nope, this is invalid" and return `False`.
# - After we finish going through the whole string, if our stack is **empty**, that means every opening bracket found its correct closing bracket. We return `True`. If it's not empty, it means we have some unmatched opening brackets, so we return `False`.

# That's it! You now have the **line-by-line** breakdown and a **visual** explanation of how the code works in the simplest way possible.

# -------------------------------------------
# Let's break down these lines step by step with an example. We'll use the string `s = "({[]})"` as our example. Imagine we're reading each character one by one and using a "stack" (a list where you add and remove items only at the end) to keep track of unmatched opening brackets.

# ---

# ### The Code in Question

# ```python
# for i in range(len(s)):        # 5
#     c = s[i]                   # 6
#     if c in closeToOpen:       # 7
#         if stack and stack[-1] == closeToOpen[c]:  # 8
#             stack.pop()        # 9
#         else:
#             return False
#     else:
#         stack.append(c)
# ```

# ---

# ### Step-by-Step Explanation with the Example `s = "({[]})"`

# | **Iteration** | **i** | **Character (c)** | **What Happens**                                                                                                                                       | **Stack (Before -> After)**               | **Explanation**                                                                                                                                                                   |
# |---------------|-------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# | **1**         | 0     | `(`               | - `c = s[0]` becomes `(`.<br>- Check: Is `(` in `closeToOpen`? (The dictionary only contains closing brackets like `)`, `]`, `}`.)                     | `[]` -> `["("]`                           | Since `(` is an **opening bracket**, it isn't a key in `closeToOpen`. So we add it to our stack. Think of it like placing a plate on top of a stack.                    |
# | **2**         | 1     | `{`               | - `c = s[1]` becomes `{`.<br>- `{` is not in `closeToOpen`, so we add it to the stack.                                                                  | `["("]` -> `["(", "{"]`                   | `{` is also an **opening bracket**, so we push it onto the stack. Now we have two unmatched opening brackets waiting to be matched later.                                       |
# | **3**         | 2     | `[`               | - `c = s[2]` becomes `[`.<br>- `[` isn't in `closeToOpen` either, so we push it onto the stack.                                                          | `["(", "{"]` -> `["(", "{", "["]`          | `[` is an **opening bracket**, so it's added to the stack. Now the stack shows the order: first `(`, then `{`, then `[`.                                                         |
# | **4**         | 3     | `]`               | - `c = s[3]` becomes `]`.<br>- Since `]` is in `closeToOpen`, we enter the `if c in closeToOpen:` block.<br>- Now we check if the stack is non-empty **and** if its last element matches the opening bracket for `]` (i.e., `closeToOpen[']']` which is `[`). | `["(", "{", "["]` -> `["(", "{"]`          | We see `]` is a **closing bracket**. We check the top of the stack (last element), which is `[`. Because `closeToOpen[']']` is also `[`, it means this `]` correctly matches the last opening bracket. We then **pop** `[` from the stack. |
# | **5**         | 4     | `}`               | - `c = s[4]` becomes `}`.<br>- `}` is in `closeToOpen`. We check the top of the stack: it is now `{`.<br>- `closeToOpen['}']` is `{`, so we pop it.      | `["(", "{"]` -> `["("]`                    | Now we see a closing bracket `}`. The top of the stack is `{` and since `closeToOpen['}']` equals `{`, it's a match. We remove `{` from the stack.                             |
# | **6**         | 5     | `)`               | - `c = s[5]` becomes `)`.<br>- `)` is in `closeToOpen`. Check the top of the stack: it is now `(`.<br>- `closeToOpen[')']` is `(`, so we pop it.       | `["("]` -> `[]`                           | Finally, we see `)`. The top of the stack is `(`, which is the matching opening bracket (since `closeToOpen[')']` equals `(`). We remove `(`, and now the stack is empty. |

# ---

# ### What the Code Is Doing

# 1. **Looping with `for i in range(len(s))`:**
#    - This line tells the program to go through each index of the string `s` from `0` to the last index.
#    - In our example, `s = "({[]})"` has 6 characters, so `i` goes from `0` to `5`.

# 2. **Accessing the Character with `c = s[i]`:**
#    - For each index `i`, we take the character at that position and call it `c`.
#    - This means on the first iteration `c` is `(`, on the second `{`, and so on.

# 3. **Checking if the Character is a Closing Bracket:**
#    - `if c in closeToOpen:` looks to see if the character is one of the closing brackets defined in our dictionary (i.e., `)`, `]`, or `}`).
#    - If it is, the code then checks if the last opening bracket in our stack matches the expected one for this closing bracket.

# 4. **Matching and Popping the Stack:**
#    - The condition `if stack and stack[-1] == closeToOpen[c]:` checks two things:
#      - **`stack`**: This ensures that there is at least one element in the stack.
#      - **`stack[-1] == closeToOpen[c]`**: This checks if the **last element** in the stack (the one on the top) is the matching opening bracket for the closing bracket `c`.
#    - If both conditions are met, `stack.pop()` is executed, which removes the top element from the stack because it has been successfully matched.

# 5. **Adding Opening Brackets to the Stack:**
#    - If `c` is not a closing bracket (i.e., it's an opening bracket), the code executes the `else` block and adds `c` to the stack with `stack.append(c)`.

# 6. **Returning the Result:**
#    - After the loop, if all opening brackets have been matched by corresponding closing brackets, the stack will be empty. The code returns `True` (or `False` if not empty).

# ---

# ### Visual Recap with the Example

# - **Initial state:** Stack is empty.
# - **After processing each character:**
#   - `(` → Stack becomes `["("]`
#   - `{` → Stack becomes `["(", "{"]`
#   - `[` → Stack becomes `["(", "{", "["]`
#   - `]` → Matches `[`, so pop: Stack becomes `["(", "{"]`
#   - `}` → Matches `{`, so pop: Stack becomes `["("]`
#   - `)` → Matches `(`, so pop: Stack becomes `[]`
# - **Final state:** Stack is empty, meaning every opening bracket was matched correctly.

# ---

# This side-by-side explanation shows both the code and the corresponding actions on the stack. The logic ensures that every time we see a closing bracket, we can verify it correctly matches the last unmatched opening bracket. If not, the code declares the string as invalid.
