#neetcode 28

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        current = root

        while current:
            # we check if the values of p and q are greater than the root value. If both are great we move to the right side of the tree.
            if p.val > current.val and q.val > current.val:
                current = current.right
                # we check if the values of p and q are less than the root value. If both are less we move to the left side of the tree.
            elif p.val < current.val and q.val < current.val:
                current = current.left

            else:
                return current

# We'll take it **line by line**, and I'll build a **mental picture** so you can *see* it in your head.

# ---

# ### First, what the heck is this code about?

# It's solving this problem:
# 👉 **Given two nodes in a Binary Search Tree (BST), find their lowest common ancestor (LCA).**

# #### What's a **Lowest Common Ancestor (LCA)**?
# Imagine a **family tree**. You and your cousin have **common grandparents**.
# The **Lowest Common Ancestor** is the **youngest** person (ancestor) in your family tree that is still **above both of you**.
# In a tree made of **numbers**, it works the same.

# ---

# ### Quick Primer on Binary Search Tree (BST):
# - Left side has **smaller** numbers
# - Right side has **bigger** numbers
# - Like a decision tree, you **go left** if smaller, **go right** if bigger

# ---

# ## Let's Break Down the Code Line by Line
# I'll keep **repeating** the concepts and **looping back** where needed to cement this.

# ---

# ### **1️⃣ Class Definition**
# ```python
# class Solution:
# ```
# 🗣️ _"Hey Python, I'm creating a **Solution box** that will hold this function."_

# Nothing much here, just a box to organize our code.

# ---

# ### **2️⃣ Function Header**
# ```python
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
# ```

# 🧠 Think of this like a recipe:
# - **root** = the starting point (the top of the tree, the big boss node)
# - **p** and **q** = the two nodes you want to find the ancestor for (like you and your cousin)

# **What do we want to find?**
# 👉 Who's the **lowest ancestor** of **both**?

# ---

# ### **3️⃣ Start the Search**
# ```python
# cur = root
# ```
# 🗣️ _"Alright, I'm standing at the **root** of the tree."_
# We'll **move around** this tree starting from the root.
# Think of `cur` as **your pointer**, where you are **currently standing** in the tree.

# ---

# ### **4️⃣ While Loop**
# ```python
# while cur:
# ```
# 🗣️ _"Keep moving around this tree **until I find** what I'm looking for."_
# As long as `cur` is **not None**, we're walking the tree.

# ---

# ### **5️⃣ First `if` condition**
# ```python
# if p.val > cur.val and q.val > cur.val:
# ```
# 🧠 **What is this saying?**
# 👉 "Hey! Are both p and q **greater** than me?"
# Imagine you're at a **fork** on the road.
# - If **both** p and q are **bigger** than where you are now…
# 👉 **Both are on the right side!**

# Visualization:
# ```
#         6   <- you're here (cur)
#        / \
#       2   8
#            \
#             9 <- p
#              \
#               10 <- q
# ```

# You and your cousin are on the **right** side of grandpa 6!
# Time to move **right**.

# ```python
# cur = cur.right
# ```
# 🗣️ _"Cool. Let's **move right**!"_
# Now `cur` points to `8` (in the example).

# ---

# ### **6️⃣ Elif Condition**
# ```python
# elif p.val < cur.val and q.val < cur.val:
# ```
# 🧠 Now the opposite:
# 👉 "Are both p and q **smaller** than me?"
# This means both of them are hanging out on the **left** side.

# Visualization:
# ```
#         6   <- you're here (cur)
#        / \
#       2   8
#      /
#     0 <- p
#    /
#  -1 <- q
# ```
# Both are on the **left** of 6.
# So:
# ```python
# cur = cur.left
# ```
# 🗣️ _"Cool. Let's **move left**!"_
# Now `cur` points to `2` (in the example).

# ---

# ### **7️⃣ Else: FOUND IT!**
# ```python
# else:
#     return cur
# ```
# 🧠 If p and q **split**, they are on **different sides** (one on the left, one on the right)...
# Or, one of them **is** the current node!
# 💡 Then you're **at their lowest common ancestor**.
# You can **stop here** and **return** this node.

# Visualization:
# ```
#         6
#        / \
#       2   8
#          /
#         7 <- p
#            \
#             8 <- q
# ```
# You're standing at `6`. One node is **left**, one node is **right**.
# `6` is the **lowest common ancestor**.

# 🗣️ _"Hey! This is the split point, or the node itself. THIS is their common ancestor!"_

# ---

# ### 🎨 Visualization Recap (Mental Picture)

# Let's use an example BST:
# ```
#         6
#        / \
#       2   8
#      / \   / \
#     0   4 7   9
#        / \
#       3   5
# ```

# #### **Example 1: p = 2, q = 8**
# - Start at **6**
# - 2 is **left**, 8 is **right**
# - ✅ Split! 6 is the **Lowest Common Ancestor**

# #### **Example 2: p = 2, q = 4**
# - Start at **6**
# - Both are **less** than 6 → move **left**
# - Now at **2**
# - 4 is **right** of 2, 2 is **itself** → ✅ 2 is the LCA

# ---

# ## ✅ Full Code with Inline Explanations (Rewritten for YOU)
# ```python
# class Solution:
#     # Find the lowest common ancestor of two nodes in a BST
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         cur = root  # Start at the top node (root)

#         while cur:  # Walk the tree until you find it

#             # If both p and q are GREATER than where you are
#             if p.val > cur.val and q.val > cur.val:
#                 cur = cur.right  # Move to the right side (bigger numbers)

#             # If both p and q are LESS than where you are
#             elif p.val < cur.val and q.val < cur.val:
#                 cur = cur.left  # Move to the left side (smaller numbers)

#             # If they split (one left, one right), or match cur
#             else:
#                 return cur  # This is their lowest common ancestor
# ```

# ---

# ### 🔁 Looping back on the Main Thought:
# - You **walk down** the tree
# - You **compare** p and q with where you are
# - If both are **bigger**, you **go right**
# - If both are **smaller**, you **go left**
# - If they **split** or match, you **found** the ancestor

# ---

# ## 🔥 Bonus Mental Trick:
# ### Think of it like **playing hot or cold**
# - "Both are on the **right**" = **colder** → go **deeper right**
# - "Both are on the **left**" = **colder** → go **deeper left**
# - "Split!" = **Bingo!** You're **hot**, found the spot!
# That's your ancestor.

# ---

# ### ✅ TL;DR (Too Lazy; Don't Read? Nah, You're Reading!)
# 👉 Move **right** if both nodes are bigger
# 👉 Move **left** if both nodes are smaller
# 👉 If they **split**, you found the **lowest common ancestor**

