#neetcode 25
class Solution(object):
    def isSameTree(self, p, q):
        # check if the both the trees are empty. If botha are empty it means they are equal
        if not p and not q:
            return True

        # check if either p or q are empty and also check if the root values of p and q are equal
        if not p or not q or p.val != q.val:
            return False

        # apply the above function to  left  and right nodes of p and q
        result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return result


#cWe're about to go *deep* into this. I'll explain it like I'm talking to someone who has *never* seen a line of code in their life.

# I'll break down every single line, show visual examples, and make sure you walk away feeling like an **absolute genius** when it comes to understanding this. 😎

# ## 🔨 **What Is This Code Trying to Do?**

# The goal of this function is to **compare two trees** and check if they are **exactly the same**.

# ### 🤔 What Does "Same Tree" Mean?
# Two trees are the **same** if:
# 1. They have the **same shape** (structure).
# 2. They have the **same values** at every corresponding node.

# If *any* difference exists (structure or values), they are **not the same**.

# ---

# ## 📜 **The Code**
# ```python
# class Solution(object):
#     def isSameTree(self, p, q):
#         # Check if both trees are empty
#         if not p and not q:
#             return True

#         # Check if one is empty OR their values are different
#         if not p or not q or p.val != q.val:
#             return False

#         # Recursively check left and right subtrees
#         result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         return result
# ```
# ---

# ## 🌳 **Visualizing the Trees**

# Let's take two trees:

# ✅ **Same Trees Example:**
# ```
#    Tree 1       Tree 2
#      1             1
#     / \           / \
#    2   3         2   3
# ```
# Both trees are **identical** in structure and values. So, the function should return `True`.

# ❌ **Different Trees Example:**
# ```
#    Tree 1       Tree 2
#      1             1
#     / \           / \
#    2   3         2   4  ❌ (Different value)
# ```
# Here, one value is different (`3` vs. `4`), so the function should return `False`.

# ---

# ## 🛠️ **Breaking It Down Line-by-Line**

# ### **1️⃣ Class Definition**
# ```python
# class Solution(object):
# ```
# 💡 We're creating a **class** called `Solution`.
# A class is like a **blueprint** for writing reusable functions.

# ---

# ### **2️⃣ Defining the Function**
# ```python
# def isSameTree(self, p, q):
# ```
# 📝 This function takes **two trees** (`p` and `q`) and checks if they are the same.

# ---

# ### **3️⃣ Checking if Both Trees Are Empty**
# ```python
# if not p and not q:
#     return True
# ```
# 🤔 **What is happening here?**

# - `p` is the first tree.
# - `q` is the second tree.
# - `not p and not q` means **both trees are empty**.
# - If both are empty, they are **identical** (because *nothing* is identical to *nothing*).

# 💡 **Example:**
# ```
# Tree 1: None
# Tree 2: None
# ```
# 👉 **Returns:** `True`

# ---

# ### **4️⃣ Checking If One Tree Is Empty or If Values Are Different**
# ```python
# if not p or not q or p.val != q.val:
#     return False
# ```
# ❓ **What does this mean?**
# We check **three** things here:
# 1. **One tree is empty, but the other isn't:**
#    - Example:
#      ```
#      Tree 1:    1
#      Tree 2:   None
#      ```
#      👉 **Returns:** `False`

# 2. **Both trees exist, but their root values are different:**
#    - Example:
#      ```
#      Tree 1:    1
#      Tree 2:    2
#      ```
#      👉 **Returns:** `False`

# ---

# ### **5️⃣ Recursively Checking Left and Right Subtrees**
# ```python
# result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# ```
# 💡 This is where **recursion** happens.

# 1. The function **calls itself** to check if the **left** sides of both trees are the same.
# 2. Then it **calls itself again** to check if the **right** sides are the same.
# 3. If **both** return `True`, we return `True`.
# 4. If **either** returns `False`, we return `False`.

# ---

# ### **6️⃣ Returning the Final Result**
# ```python
# return result
# ```
# - If **both left and right sides are the same**, return `True`.
# - Otherwise, return `False`.

# ---

# ## 🔁 **How the Function Works Step-by-Step**

# Let's take two trees and walk through each step of the function.

# ```
#    Tree 1       Tree 2
#      1             1
#     / \           / \
#    2   3         2   3
# ```

# ### **Step 1: Checking the Root**
# - `p = 1`, `q = 1`
# - They **match**, so we continue.

# ### **Step 2: Check Left Subtree (`p.left = 2`, `q.left = 2`)**
# - They **match**, so we go **deeper** into their children.
# - `p.left.left = None`, `q.left.left = None` → `True`
# - `p.left.right = None`, `q.left.right = None` → `True`

# ✅ Left side is **OK**.

# ### **Step 3: Check Right Subtree (`p.right = 3`, `q.right = 3`)**
# - They **match**, so we check their children.
# - `p.right.left = None`, `q.right.left = None` → `True`
# - `p.right.right = None`, `q.right.right = None` → `True`

# ✅ Right side is **OK**.

# ### **Final Answer:**
# - Left subtree is **same** (`True`).
# - Right subtree is **same** (`True`).
# - So, the function returns **`True`**. ✅

# ---

# ## 🚀 **Recap of Key Takeaways**
# 1. **We check if both trees are empty** → `True` if yes.
# 2. **If one tree is empty but the other isn't, they are not the same.**
# 3. **If root values are different, return `False`.**
# 4. **We check both left and right subtrees using recursion.**
# 5. **If both left and right are the same, the whole tree is the same!**

# ---

# ## ✏️ **Practice Time!**
# Try checking these trees:

# ```
#    Tree 1       Tree 2
#      1             1
#     / \           / \
#    2   3         2   4
# ```
# 👉 What will the function return?

# Answer: **`False`**, because `3` ≠ `4`.


