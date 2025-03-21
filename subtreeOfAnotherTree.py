#neetcode 26
class Solution(object):
    def isSubtree(self, root, subRoot):
        # check if the subroot here is empty or not. If it is empty it means it is 100% a subtree of the main tree
        if not subRoot:
            return True

            # check if the main tree is empty if the main tree is empty then the subroot is not present in the main tree
        if not root:
            return False

        # check if the subtree is present in the main tree
        if self.isSameTree(root, subRoot):
            return True

            # if all the conditions fail above we check if the left childo or right child contains the sub tree
        result = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return result

    def isSameTree(self, p, q):
        # check if the trees p and q are both empty. If they are empty they are equal
        if not p and not q:
            return True

        # check if either of  the trees are empty if one of them is empty the they are not same or equal also check if the values of the trees and if they don't they are not same or equal
        if not p or not q or p.val != q.val:
            return False

        result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return result

#I'll explain how the code works step by step, in plain English. I'll even help you visualize it because you asked for it!

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