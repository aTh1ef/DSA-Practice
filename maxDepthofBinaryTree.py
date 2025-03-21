#neetcode 24
#recursive method
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        answer = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return answer

#Let's go step-by-step, breaking this code down to its bones, and I'll help you visualize it with a tree example. Let's get this super clear!

# ---

# ## 🔨 The Code You Shared

# ```python
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0

#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# ```

# ---

# ## 🌳 What's This Code Trying to Do?
# It's finding **how tall** a tree is.

# Think of the tree as a family tree or a hierarchy chart:
# - The **height** is the longest line from the **top person** (the root node) all the way **down to the bottom person** (the leaf node).

# In technical words:
# We are calculating the **maximum depth** of a **binary tree**.

# ---

# ## 🖼️ Visual Example: The Tree

# ```
#        1
#       / \
#      2   3
#     / \
#    4   5
# ```

# Here's how the tree works:
# - `1` is the **root** (the boss, the top node).
# - `1` has two children: `2` and `3`.
# - `2` has two children: `4` and `5`.
# - `3` has **no** children (poor lonely node 😢).

# 👉 The depth from `1 -> 2 -> 4` is **3**
# 👉 The depth from `1 -> 3` is **2**

# The **max depth** is **3** because the longest path from top to bottom has **3 nodes**.

# ---

# ## 🛠️ Let's Walk Line-by-Line Through the Code (Like a Detective 🕵️‍♂️)

# ---

# ### `class Solution:`

# We're creating a **blueprint** or **template** for solving this problem. Think of it as creating a toolbox that has this magical method (`maxDepth`) inside.

# ---

# ### `def maxDepth(self, root: TreeNode) -> int:`

# We're making a **function** called `maxDepth`.
# It takes in:
# 1. `self`: Standard Python stuff (just trust us on this one 😅).
# 2. `root`: The **current node** we're standing on in the tree.

# 👉 **`TreeNode`** means we're dealing with a node in the tree.
# Each node can have:
# - A **left** child.
# - A **right** child.

# ---

# ### `if not root:`

# We're saying:
# 👀 "Is the node **empty**? Is it **None**? Is there **nothing here**?"
# This means we're at the **bottom** of a branch, and there's **no more nodes**.

# ---

# ### `return 0`

# If we hit a **dead-end** (no node exists), the **depth** at this point is **0**.

# ---

# ### `return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))`

# This is the **meat**.
# We're saying:
# - Start counting from `1` (because we're standing **on a node** right now).
# - Then ask:
# 👉 "How deep is the **left side**?"
# 👉 "How deep is the **right side**?"

# 👉 Take the **maximum** of both, because we only care about the **longest path**!

# ---

# ## 🔁 What Happens When We Run This on Our Tree?

# Let's use **this tree** again:

# ```
#        1
#       / \
#      2   3
#     / \
#    4   5
# ```

# ---

# ### 🟢 First Call: `maxDepth(1)`
# We're on node **1**.

# 1. Is `root` empty? **No.**
# 2. We go **left** to `2` and **right** to `3`.
# 3. We need the **maximum depth** between left and right.

# ---

# ### 🟢 Left Call: `maxDepth(2)`
# We're on node **2**.

# 1. Is `root` empty? **No.**
# 2. We go **left** to `4` and **right** to `5`.
# 3. We need the **maximum depth** between them.

# ---

# ### 🟢 Left Call of Left: `maxDepth(4)`
# We're on node **4**.

# 1. Is `root` empty? **No.**
# 2. Both **left** and **right** are empty.
# 3. We do:
#    ```
#    return 1 + max(0, 0) = 1
#    ```

# ---

# ### 🟢 Right Call of Left: `maxDepth(5)`
# We're on node **5**.

# 1. Same as node `4`. Both **left** and **right** are empty.
# 2. We do:
#    ```
#    return 1 + max(0, 0) = 1
#    ```

# ---

# Now back to node **2**.
# We have:
# ```
# return 1 + max(1, 1) = 2
# ```

# ---

# ### 🟢 Right Call: `maxDepth(3)`
# We're on node **3**.

# 1. Left and right are empty.
# 2. We do:
#    ```
#    return 1 + max(0, 0) = 1
#    ```

# ---

# ### 🟢 Back to node 1
# Now we have:
# ```
# return 1 + max(2, 1) = 3
# ```

# ---

# ## ✅ Final Answer: `3`

# The **maximum depth** of the tree is **3**.

# ---

# ## 🔨 Visualizing the Recursive Calls (Like a Call Stack)

# ```
# maxDepth(1)
# ├── maxDepth(2)
# │   ├── maxDepth(4) = 1
# │   └── maxDepth(5) = 1
# │   -> 1 + max(1, 1) = 2
# └── maxDepth(3) = 1
# -> 1 + max(2, 1) = 3
# ```

# ---

# ## 💡 How to Think of It (Real Life)

# Imagine you're standing at the top of a tree.
# You send two ants:
# - One goes **left**.
# - One goes **right**.

# They both go down as far as they can.
# You ask them: "How far did you go?"
# You take the answer of the one who went the **furthest**, and you add **1** because **you** were at the top.

# ---

# ## 📜 Final Code (With Comments)

# ```python
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         # If there's no node, the depth is 0
#         if not root:
#             return 0

#         # Go left, go right, take the deeper one, and add 1 for the current node
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# ```

# ---

# ## 🔥 Recap of Key Points
# 1. We're finding the **maximum depth** of a binary tree.
# 2. We do it by **recursively** going down **both sides** of each node.
# 3. We **return 0** when we hit a dead end (no node).
# 4. We take the **maximum** depth of left and right and **add 1** at each level.
# 5. The **final number** tells you how many levels deep the tree goes!

# ---

# ## ✏️ You Try!
# Try this one:

# ```
#        10
#        /
#      20
#      /
#    30
# ```

# What's the depth?
# 👉 Start at `10`: Go left to `20`
# 👉 `20`: Go left to `30`
# 👉 `30`: No more kids!
# How many levels?
# 👉 Answer: **3**