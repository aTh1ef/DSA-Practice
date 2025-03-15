#neetcode 24

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# ### **Step 1: What the heck is DFS?**

# ✅ **DFS stands for Depth-First Search.**

# Imagine you're in a mansion with lots of rooms and doors. Instead of checking every room on the ground floor first, you decide:
# *"I'll pick a door, go as deep as I can, even if it takes me to the basement, and only when I hit a dead-end, I'll come back and check the next door!"*

# DFS does the same thing—but with trees (not the ones in the park, though 🌳).

# ---
# ### **Step 2: What's a Tree in Programming?**

# It's like a family tree!
# - There's a **root** (grandpa).
# - He has children (your dad and uncle).
# - They can have their own kids.
# You can go from one person to their descendants (down the tree).

# But instead of family members, we're dealing with **nodes** that have:
# - A **left child**
# - A **right child**

# A tree in programming **always starts at the root** and branches out.

# ---
# ### **Step 3: What is "Invert a Tree"?**

# It's like flipping the tree **left to right**.

# #### Imagine this tree:
# ```
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
# ```

# After inverting, it looks like this:
# ```
#        1
#      /   \
#     3     2
#    / \   / \
#   7   6 5   4
# ```

# All **left kids become right**, and **right kids become left**.

# ---
# ### **Step 4: Let's Dive Into the Code**

# Here's your code:
# ```python
# class Solution(object):              # 1
#     def invertTree(self, root):      # 2
#         if not root:                 # 3
#             return None              # 4

#         tmp = root.left              # 5
#         root.left = root.right       # 6
#         root.right = tmp             # 7

#         self.invertTree(root.left)   # 8
#         self.invertTree(root.right)  # 9

#         return root                  # 10
# ```

# ---

# ### **Now Let's Walk Through It Step by Step Like a Movie Scene**

# #### **Scene 1: We meet the Solution class**
# ```python
# class Solution(object):
# ```
# This is like building a toolbox called `Solution`.
# Inside it, we'll have a tool (a function) called `invertTree`.

# #### **Scene 2: Defining the invertTree function**
# ```python
# def invertTree(self, root):
# ```
# We're saying:
# *"Hey! Give me the root of your tree, and I'll flip it!"*

# The `root` is the current node we're looking at.
# At the beginning, it's the **top** of the tree.

# ---

# ### **Scene 3: The Base Case - We Check for Nothingness**
# ```python
# if not root:
#     return None
# ```

# 👉 Think of this like knocking on a door and seeing… **nothing** behind it.
# There's no tree to flip.
# So, we say:
# *"Ah, there's nothing here. Let's go back!"*

# If `root` is `None` (empty), we just leave.

# ---

# ### **Scene 4: We Swap the Kids**
# ```python
# tmp = root.left
# ```
# You *grab* the **left child** and **hold it in your hand** (temporary storage).
# Like:
# *"Yo, left kid, stand here for a second!"*

# ---
# ```python
# root.left = root.right
# ```
# You *point the left door to the right kid*.
# Like:
# *"Left, go where the right kid was!"*

# ---
# ```python
# root.right = tmp
# ```
# You take the **original left kid** (who was standing aside) and tell them:
# *"Now you go to the right!"*

# ---

# ### **Scene 5: Dive Into the Left Side**
# ```python
# self.invertTree(root.left)
# ```
# Now you tell yourself:
# *"Ok, I swapped the kids here. Now let me walk through that **new** left door and keep doing the same thing there."*

# This is where **DFS** happens.
# You go **deep** into the left child and repeat everything from Scene 3 onward.

# ---

# ### **Scene 6: Dive Into the Right Side**
# ```python
# self.invertTree(root.right)
# ```
# When you've finished the left side, you come back and do the same for the **right** child.

# ---

# ### **Scene 7: Return The Flipped Tree**
# ```python
# return root
# ```
# After you've flipped the current node *and* flipped all its left and right subtrees, you hand it back.

# ---

# ### **Visual Walkthrough**

# #### Original Tree:
# ```
#        1
#      /   \
#     2     3
# ```

# #### Step 1: Start at root (1)
# - `tmp = 2`
# - `root.left = 3`
# - `root.right = tmp (2)`

# Now the tree looks like:
# ```
#        1
#      /   \
#     3     2
# ```

# #### Step 2: Go into root.left (which is now 3)
# - It has no children (assume empty)
# - Swap left/right → no change
# - Done.

# #### Step 3: Go into root.right (which is now 2)
# - It has no children
# - Swap left/right → no change
# - Done.

# #### Result:
# ```
#        1
#      /   \
#     3     2
# ```

# ---
# ### **Full Visual Example (Big Tree)**

# #### Starting Tree:
# ```
#         4
#       /   \
#      2     7
#     / \   / \
#    1   3 6   9
# ```

# #### Steps:
# 1. At node `4`:
#    - Swap `2` and `7`
# 2. Go left to `7`:
#    - Swap `6` and `9`
# 3. Go left to `9`:
#    - No kids, done.
# 4. Go right to `6`:
#    - No kids, done.
# 5. Back to node `2`:
#    - Swap `1` and `3`
# 6. Go left to `3`:
#    - No kids, done.
# 7. Go right to `1`:
#    - No kids, done.

# #### Final Inverted Tree:
# ```
#         4
#       /   \
#      7     2
#     / \   / \
#    9   6 3   1
# ```

# ---
# ### **Summary:**

# - You walk down the tree **one path at a time** (DFS).
# - At each node:
#   1. Swap left and right.
#   2. Go as deep as possible on the new left.
#   3. Come back and do the new right.
# - Repeat until done.

# ---
# ### **Mental Model (for Visualization):**

# - Pretend each **node is a house**.
# - **Left and right children are doors**.
# - You **swap** where those doors go.
# - Then you **walk through the left door**, repeat.
# - Then **walk through the right door**, repeat.

# ---
# ### **Boom. Done.**