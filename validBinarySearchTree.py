#neetcode 30

class Solution(object):
    def isValidBST(self, root):

        # creating a helper function cuz we chill like that
        def valid(node, left, right):

            # if the node is empty we return True
            if not node:
                return True

            # if the node is not greater than the left child or not less than the right child we are cooked so we return False
            if not (left < node.val < right):
                return False

                # keep checking the left and right subtrees with updated boundaries
            result = valid(node.left, left, node.val) and valid(node.right, node.val, right)
            return result

        # starting the recursion with the whole range
        return valid(root, float("-inf"), float("inf"))

    # # ✅ What are we doing?
    # We are **checking** if a **Binary Search Tree (BST)** is actually a **valid BST**.
    # Like checking if a kid's homework is done *by the rules*.

    # ---

    # ## What's a Binary Search Tree (BST)?
    # A **BST** is a **binary tree** that follows **two golden rules**:

    # 1. Every node's **left child** has a **smaller** value.
    # 2. Every node's **right child** has a **bigger** value.

    # ### Here's a valid BST:
    # ```
    #        5
    #      /   \
    #     3     7
    #    / \   / \
    #   2  4  6  8
    # ```
    # - Left < Parent < Right
    # - Works at **every** node.

    # ---

    # ## 🎯 The Goal:
    # Write a **function** to **check** if the tree you get **follows the BST rules**.

    # ---

    # ---

    # # 🔥 Let's take the code and explain it like we're making a sandwich.

    # ## Step 1️⃣ — Setup
    # ```python
    # class Solution:
    # ```
    # Think of this as **naming your team**.
    # Team "Solution" is going to solve the problem.

    # ---

    # ```python
    # def isValidBST(self, root: TreeNode) -> bool:
    # ```
    # You're writing a **method** (function inside a class) called `isValidBST`.
    # This thing will take the **root** of a tree and tell you **True or False**.
    # - True = "Yeah, man! It's a valid BST!"
    # - False = "Nope. Someone broke the rules."

    # ---

    # ---

    # # 🔧 Step 2️⃣ — Make the Worker Function (The Actual Validator)
    # ```python
    # def valid(node, left, right):
    # ```
    # You're defining a **helper function**, `valid`, inside `isValidBST`.
    # This is the **dude who does the checking**.
    # - `node` → The current node you're looking at.
    # - `left` → The **minimum** allowed value.
    # - `right` → The **maximum** allowed value.

    # ### 🎯 Its job:
    # For every `node`, check:
    # "Are you **greater** than `left` and **less** than `right`?
    # If yes → Cool.
    # If no → Fail."

    # ---

    # ---

    # ## 🧠 Step 3️⃣ — Base case: If there's no node
    # ```python
    # if not node:
    #     return True
    # ```
    # Imagine you're walking through the tree.
    # You hit a **dead end** (no node).
    # What's that mean?
    # ✅ That part of the tree **didn't break any rules**.
    # So we say **True**, and move on.

    # ---

    # ---

    # ## 🚨 Step 4️⃣ — Break the Rule?
    # ```python
    # if not (node.val < right and node.val > left):
    #     return False
    # ```
    # Translation:
    # - "Hey node! Are you **between** your boundaries (`left` and `right`)?"

    # ### Examples:
    # If your node is **5**,
    # - `left` = 3
    # - `right` = 7
    # Then it better be:
    # ```
    # left < node.val < right
    # 3  <   5      < 7  ✅
    # ```

    # But if it's **10**?
    # ```
    # 3 < 10 < 7 ❌ Nooope!
    # ```
    # We scream:
    # ❌ "You broke the rule!"
    # And return **False**.

    # ---

    # ---

    # ## 🔁 Step 5️⃣ — Recursion Time (The Crazy Part)
    # ```python
    # return (
    #     valid(node.left, left, node.val) and
    #     valid(node.right, node.val, right)
    # )
    # ```
    # We now **check both kids**:
    # - Left Child → Needs to stay **between** the parent's left boundary and the parent's value.
    # - Right Child → Needs to stay **between** the parent's value and the parent's right boundary.

    # ### 🎯 What's happening?
    # When you go **left**, you tighten the **right** boundary:
    # - It can't go **bigger** than `node.val`.

    # When you go **right**, you tighten the **left** boundary:
    # - It can't go **smaller** than `node.val`.

    # ---

    # ---

    # ## 🚀 Step 6️⃣ — Start the Engine
    # ```python
    # return valid(root, float("-inf"), float("inf"))
    # ```
    # We **kick things off** with the **root node**.
    # But we give it **no limits**:
    # - Left limit? **Negative infinity** → Go as small as you like.
    # - Right limit? **Infinity** → Go as big as you like.

    # ---

    # ---

    # # 🧰 The Full Code (In Human Speak)

    # ```python
    # class Solution:
    #     def isValidBST(self, root: TreeNode) -> bool:
    #         def valid(node, left, right):                # 🧑‍🔧 helper function
    #             if not node:                              # 🕳️ hit a dead end?
    #                 return True                           # ✅ no problem!
    #             if not (node.val < right and node.val > left):  # 🚨 out of bounds?
    #                 return False                          # ❌ rule broken!
    #             return (
    #                 valid(node.left, left, node.val)      # 👈 left kid
    #                 and
    #                 valid(node.right, node.val, right)    # 👉 right kid
    #             )
    #         return valid(root, float("-inf"), float("inf"))  # 🚀 start here!
    # ```

    # ---

    # ---

    # # 🧠 DEEP VISUALIZATION
    # ## We need an example tree, right?

    # Let's roll with:
    # ```
    #        10
    #       /  \
    #      5   15
    #         /  \
    #       12   20
    # ```

    # ---

    # ### 1️⃣ Call: `valid(10, -inf, inf)`
    # - node = 10
    # - left = -inf
    # - right = inf
    # ```
    # Is 10 > -inf and < inf? ✅ YES
    # ```
    # Now we check its kids!
    # ---
    # ### 2️⃣ Left kid: `valid(5, -inf, 10)`
    # - node = 5
    # - left = -inf
    # - right = 10
    # ```
    # Is 5 > -inf and < 10? ✅ YES
    # ```
    # Now check 5's kids (none).
    # ✅ Return True for left.
    # ---
    # ### 3️⃣ Right kid: `valid(15, 10, inf)`
    # - node = 15
    # - left = 10
    # - right = inf
    # ```
    # Is 15 > 10 and < inf? ✅ YES
    # ```
    # Now check 15's kids.
    # ---
    # ### 4️⃣ Left of 15: `valid(12, 10, 15)`
    # - node = 12
    # - left = 10
    # - right = 15
    # ```
    # Is 12 > 10 and < 15? ✅ YES
    # ```
    # ✅ Return True
    # ---
    # ### 5️⃣ Right of 15: `valid(20, 15, inf)`
    # - node = 20
    # - left = 15
    # - right = inf
    # ```
    # Is 20 > 15 and < inf? ✅ YES
    # ```
    # ✅ Return True
    # ---
    # All checks passed!
    # ✅ This tree is a valid BST!

    # ---

    # ---

    # # ❌ BROKEN EXAMPLE (The FAIL CASE!)
    # ### Tree:
    # ```
    #        10
    #       /  \
    #      5   15
    #         /  \
    #       6    20
    # ```
    # Wait. **6 is on the right of 10**, but it's **less than 10**!
    # That breaks the rule!

    # ---

    # ### 1️⃣ Call: `valid(10, -inf, inf)` ✅
    # ### 2️⃣ Left kid: `valid(5, -inf, 10)` ✅
    # ### 3️⃣ Right kid: `valid(15, 10, inf)` ✅
    # ### 4️⃣ Left of 15: `valid(6, 10, 15)`
    # ```
    # Is 6 > 10 and < 15? ❌ NO!
    # ```
    # We return **False**, the tree is broken!

    # ---

    # ---

    # # 🖼️ VISUAL MAP
    # Here's a **brain map** of how it works:
    # ```
    #                    10
    #                  /    \
    #               5          15
    #                        /    \
    #                     12        20

    # valid(10, -inf, inf)
    #     ├─ valid(5, -inf, 10) ✅
    #     └─ valid(15, 10, inf) ✅
    #         ├─ valid(12, 10, 15) ✅
    #         └─ valid(20, 15, inf) ✅
    # ```

    # ---

    # ---

    # # 🧽 Quick Recap for a Potato (or Me on a Bad Day)

    # | Concept                  | Dumbed Down Version                         |
    # |--------------------------|--------------------------------------------|
    # | BST                      | Left < Parent < Right. No exceptions.      |
    # | valid(node, left, right) | "Stay between the lines, kid!"             |
    # | node.val < right         | "Don't go bigger than your right limit!"   |
    # | node.val > left          | "Don't go smaller than your left limit!"   |
    # | valid(left)              | Move left, **tighten right boundary**      |
    # | valid(right)             | Move right, **tighten left boundary**      |
    # | Return True              | "All good here!"                           |
    # | Return False             | "You broke the rule!"                      |


# ## 🌳 Problem Recap (Visualize It!)
#
# We have two trees:
# - **Big Tree** (called `root`): This is your main tree.
# - **Small Tree** (called `subRoot`): You want to check if this tree is hiding *inside* the big tree.
#
# Imagine the big tree is like a giant family tree 📜, and you are looking to see if one of the branches (subtrees) is an exact copy of the small tree.
#
# ---
#
# ## ✅ Step 1: Understand What We're Doing
# We're trying to answer this question:
# > "Does the big tree `root` have a spot somewhere that looks exactly like the smaller tree `subRoot`?"
#
# And we do that by:
# 1. Walking through every node of the big tree (`root`).
# 2. At each node, asking:
#    **"Hey! Do you look like `subRoot`?"**
#    If yes, we're done. If not, we keep looking at the left and right children.
#
# ---
#
# ## 👨‍🏫 Walkthrough the Code Line by Line
# (With comments and dumb-friendly explanation!)
#
# ---
#
# ```python
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# ```
# ### What's happening here?
# ➡️ This is the basic structure of a tree node.
# Think of it as a little box 📦 that:
# - Holds a value (`val`)
# - Has a left child (`left`)
# - Has a right child (`right`)
# A binary tree is just a bunch of these boxes linked together.
#
# ---
#
# ## 🔨 Now the real work begins...
# ```python
# class Solution(object):
# ```
# ➡️ This is just making a new class where we put our functions (methods).
#
# ---
#
# ### Function 1: `isSubtree`
# ```python
#     def isSubtree(self, root, subRoot):
# ```
# ➡️ We're making a function called `isSubtree`.
# Its job is to check if `subRoot` is somewhere inside `root`.
#
# ---
#
# ### Step 1: If subRoot is empty...
# ```python
#         # check if subRoot is empty (None). If it's empty, it's automatically a subtree!
#         if not subRoot:
#             return True
# ```
# ➡️ Picture this:
# If I ask you:
# > "Hey, is **nothing** (an empty tree) inside your big tree?"
# The answer is always "Yes!" ✅ because *nothing* is always inside something.
#
# ---
# ### Step 2: If the big tree is empty...
# ```python
#         # if the big tree root is empty but subRoot isn't, subRoot can't be there!
#         if not root:
#             return False
# ```
# ➡️ If the big tree `root` doesn't exist (it's empty), and we're looking for a non-empty `subRoot`, it's impossible to find it.
# It's like saying:
# > "Can I find a tree inside an empty field?" 🌲❌
# Nope. So return False.
#
# ---
#
# ### Step 3: Do these two trees look exactly the same **at this spot**?
# ```python
#         # check if the subtree starting from here is exactly the same as subRoot
#         if self.isSameTree(root, subRoot):
#             return True
# ```
# ➡️ We check:
# > "Does this node of the big tree look **exactly** like `subRoot`?"
# If yes, we found our match! 🎉 Return True.
#
# ---
#
# ### Step 4: If no match here, check left and right children...
# ```python
#         # if not, check the left and right child nodes
#         result = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
#         return result
# ```
# ➡️ If this node doesn't match `subRoot`, we move down the tree:
# 👉 Check the left child
# 👉 Check the right child
# If either side has `subRoot`, we're happy and return True.
#
# ---
#
# ---
#
# ## 🌳 Function 2: `isSameTree`
# ➡️ This helper function checks if two trees are **exactly the same**.
#
# ---
#
# ### Function declaration
# ```python
#     def isSameTree(self, p, q):
# ```
# ➡️ `p` and `q` are two trees we want to compare.
#
# ---
#
# ### Step 1: Are both empty?
# ```python
#         # check if both p and q are None (empty). If they are, they are the same!
#         if not p and not q:
#             return True
# ```
# ➡️ If both trees are empty, they are obviously the same (both are nothing).
#
# ---
#
# ### Step 2: Is one of them empty or do they have different values?
# ```python
#         # if one is empty and the other isn't, or they have different values, they aren't the same
#         if not p or not q or p.val != q.val:
#             return False
# ```
# ➡️ If one tree is empty and the other isn't—different! ❌
# If their values don't match—different! ❌
#
# ---
#
# ### Step 3: Compare their children (left and right)
# ```python
#         # check if their left subtrees and right subtrees are also the same
#         result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         return result
# ```
# ➡️ We dive deeper:
# 👉 Are their left children exactly the same?
# 👉 Are their right children exactly the same?
# If both are True, the trees are the same. ✅
#
# ---
#
# ---
#
# ## 🧠 Deep Visualization
# Let me paint a scene in your head:
#
# - Imagine `root` is a big family tree.
# - Imagine `subRoot` is a branch you cut out and you're trying to tape it back into the big tree, somewhere.
# - You start at the top of the big tree and work your way down.
# At each point, you ask:
# 👉 "Does this branch look *exactly* like the one I'm holding?"
# - If yes, cool, done!
# - If not, go down the left side and then the right side.
#
# The **`isSameTree()`** function is like taking a microscope 🔬 and comparing every leaf and twig on two branches to see if they're *exactly* the same.
#
# ---
#
# ---
#
# ## ✅ Your Comments Feedback
#
# What you wrote:
# ```python
#     # check if the both the trees are empty. If botha are empty it means they are equal
# ```
# ✅ Good! I'd maybe clean up the English just a bit for clarity:
# ➡️ "Check if both trees are empty. If they are, they are considered equal."
#
# What you wrote:
# ```python
#     # check if either p or q are empty and also check if the root values of p and q are equal
# ```
# ✅ Nice! Could make it clearer:
# ➡️ "If one of them is empty or their values are not the same, they are not equal."
#
# ---
#
# ---
#
# ## 🔥 Full Code With Ultra Clear Comments
#
# ```python
# # Definition for a binary tree node.
# # This class defines how a single node of a tree looks.
# # Each node has a value and pointers to the left and right children.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
#
# class Solution(object):
#     def isSubtree(self, root, subRoot):
#         # If subRoot is None, it means we're looking for an empty tree.
#         # An empty tree is always a subtree!
#         if not subRoot:
#             return True
#
#         # If root is None but subRoot isn't, there's no way subRoot can be here.
#         if not root:
#             return False
#
#         # Check if the current node in root is the start of a tree
#         # that looks exactly like subRoot
#         if self.isSameTree(root, subRoot):
#             return True
#
#         # If not, we keep searching on the left and right subtrees.
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
#
#     def isSameTree(self, p, q):
#         # If both nodes are None, we reached the end together—trees are equal here.
#         if not p and not q:
#             return True
#
#         # If one node is None and the other isn't, or the values don't match, they are not the same.
#         if not p or not q or p.val != q.val:
#             return False
#
#         # Recursively check if the left subtrees AND right subtrees are the same.
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# ```
#
# ---
#
# ## 🎨 Visual Summary
# Imagine:
# ```
# Big Tree (root):
#          3
#         / \
#        4   5
#       / \
#      1   2
#
# Sub Tree (subRoot):
#        4
#       / \
#      1   2
# ```
#
# You start at `3` and say:
# "Do you look like `subRoot`?"
# Nope.
#
# Go to the left child `4`.
# "Do you look like `subRoot`?"
# Yes! Let's check the children.
# Left: `1` == `1` ✅
# Right: `2` == `2` ✅
# It's a match! We found the subtree!
