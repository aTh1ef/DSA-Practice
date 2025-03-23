#neetcode31
class Solution(object):
    def kthSmallest(self, root, k):
        curr = root
        #create a stack
        stack = []

        #loop till the stack is empty
        while stack or curr:
            #loop till we do not have any current value
            while curr:
                stack.append(curr)
                curr = curr.left
            #if the current node value is null we pop the current element or value
            curr = stack.pop()
            k -= 1

            #now we implement the condition; if the k value reaches 0 we have found the kth element
            if k == 0:
                return curr.val

            curr = curr.right

# ### 🚀 **What's Happening in this Code?**

# This code finds the **k-th smallest element** in a **Binary Search Tree (BST)**.

# - **BST Rule**: Left child is smaller, right child is bigger.
# - So, **if you walk through it in order (Left → Node → Right)**, you get the numbers in **sorted order**.

# ---

# ### 🧠 **High-Level Plan**

# The code does an **in-order traversal**:
# - Go as left as possible.
# - Visit the node (this gives us "sorted" numbers).
# - Go right.

# While doing this, we **count nodes**. When we hit the **k-th node**, we **return** it.

# ---

# ## ✅ Step-by-Step Code and Visualization

# We'll go **line by line** with **visualization**, like we're sitting with a whiteboard.

# ---

# ---

# # **Code**
# ```python
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
# ```

# ### ✅ Step 1 — **We're defining a function.**

# - **`root`** is the start of your tree.
# - **`k`** is which smallest number you want.

# ---

# ---

# # **Code**
# ```python
#         stack = []
# ```

# ### ✅ Step 2 — **We create an empty stack.**

# 📝 **Stack** = like a pile of plates. You put things **on top** (`append`), and you take them **off the top** (`pop`).

# We'll use it to **remember nodes** as we go deep into the tree.

# ---

# ---

# # **Code**
# ```python
#         curr = root
# ```

# ### ✅ Step 3 — **Start at the root node**.

# This is where our journey begins.

# ---

# ### 🖼️ **Visualization Start: Tree Example**

# Let's work with this tree👇:

# ```
#         5
#        / \
#       3   6
#      / \
#     2   4
#    /
#   1
# ```

# And we'll try to find **k = 3**, meaning **the 3rd smallest**.

# ---

# ---

# # **Code**
# ```python
#         while stack or curr:
# ```

# ### ✅ Step 4 — **Loop while we have nodes to visit.**

# As long as:
# - There's something in the **stack** (stuff we haven't processed yet), OR
# - `curr` points to **a node** (we haven't visited yet),

# 👉 **We keep going**.

# ---

# ---

# # **Code**
# ```python
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
# ```

# ---

# ### ✅ Step 5 — **Go as far LEFT as possible.**

# ### 🔥 THE MEAT OF THE IN-ORDER TRAVERSAL 🔥

# #### First Run:
# - Start at **curr = 5** ➡️ Push it on the stack ➡️ Go left to **3**.
# - curr = 3 ➡️ Push on stack ➡️ Go left to **2**.
# - curr = 2 ➡️ Push on stack ➡️ Go left to **1**.
# - curr = 1 ➡️ Push on stack ➡️ Go left to `None`.

# ### 🖼️ **Stack after this**:
# ```
# [5, 3, 2, 1]
# ```

# #### curr is now `None`. We can't go further left.

# ---

# ---

# # **Code**
# ```python
#             curr = stack.pop()
# ```

# ### ✅ Step 6 — **Pop from the stack (visit a node).**

# #### First Pop:
# - Pop **1** from the stack.

# Now, **curr** points to **1**.

# ---

# ---

# # **Code**
# ```python
#             k -= 1
# ```

# ### ✅ Step 7 — **Subtract 1 from k.**

# - We just **visited** the **1st smallest** (because this is in-order).
# - k was 3, now **k = 2**.

# ---

# ---

# # **Code**
# ```python
#             if k == 0:
#                 return curr.val
# ```

# ### ✅ Step 8 — **Check if k == 0.**

# Not yet! k is **2**, so keep going.

# ---

# ---

# # **Code**
# ```python
#             curr = curr.right
# ```

# ### ✅ Step 9 — **Go to the RIGHT child.**

# Node **1** doesn't have a right child → curr = `None`.

# ---

# ---

# ### 🔁 **Loop Back to Step 4!**

# **stack** still has stuff in it.

# ### 🖼️ **Current Stack**:
# ```
# [5, 3, 2]
# ```

# ---

# ---

# ## ✅ 2nd Round of the Loop

# ### Step 5 — `curr` is `None`, so skip inner loop.

# ### Step 6 — `curr = stack.pop()` ➡️ Pop **2**.

# ### Step 7 — `k -= 1` ➡️ k becomes **1**.

# ### Step 8 — k != 0, so move on.

# ### Step 9 — `curr = curr.right` ➡️ curr = `None` (2 has no right child).

# ---

# ---

# ### 🔁 **Loop Back to Step 4 Again!**

# ### Step 6 — Pop **3** from stack.

# ### Step 7 — `k -= 1` ➡️ k becomes **0**.

# ---

# ---

# # **We Found It!**

# ### Step 8 — `if k == 0` ➡️ YES!
# We return `curr.val`.

# ### curr is **3** ➡️ This is the **3rd smallest element**.

# ✅ **Answer = 3**.

# ---

# ---

# ---

# ## 🧠 **Step-by-Step Recap with Visualization**
# (Imagine you're walking the tree like this)

# | Step | Current Node | Stack            | k  | Action                     |
# |------|--------------|------------------|----|----------------------------|
# | 1    | 5            | []               | 3  | Push 5, go left            |
# | 2    | 3            | [5]              | 3  | Push 3, go left            |
# | 3    | 2            | [5, 3]           | 3  | Push 2, go left            |
# | 4    | 1            | [5, 3, 2]        | 3  | Push 1, go left → None     |
# | 5    | None         | [5, 3, 2, 1]     | 3  | Pop 1 → visit → k = 2      |
# | 6    | None         | [5, 3, 2]        | 2  | Pop 2 → visit → k = 1      |
# | 7    | None         | [5, 3]           | 1  | Pop 3 → visit → k = 0 ✅    |
# | 8    | Return       |                  |    | Return 3 ✔                |

# ---

# ---

# ## 🎨 **Another Visualization (In-Order Walk)**
# ```
#          5
#        /   \
#       3     6
#      / \
#     2   4
#    /
#   1
# ```

# ➡️ **Visit Order (In-Order Traversal)**
# 1 ➡️ 2 ➡️ 3 ➡️ 4 ➡️ 5 ➡️ 6

# - k = 1 → 1
# - k = 2 → 2
# - k = 3 → 3 ✅
# - k = 4 → 4
# - k = 5 → 5
# - k = 6 → 6

# ---

# ---

# ## 🛠️ **Code Again with Dumbass-Friendly Comments**
# ```python
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         # Stack to keep track of nodes
#         stack = []

#         # Start with the root node
#         curr = root

#         # Go until there's no node left or nothing in the stack
#         while stack or curr:

#             # Go as left as possible, keep putting nodes on the stack
#             while curr:
#                 stack.append(curr)  # Save the node
#                 curr = curr.left    # Move left

#             # Pop the last saved node (most recent)
#             curr = stack.pop()

#             # We visited one more node in order
#             k -= 1

#             # If this is the k-th smallest, return its value!
#             if k == 0:
#                 return curr.val

#             # Move to the right subtree to continue traversal
#             curr = curr.right
# ```

# ---

# ---

# ## 🧩 **Why Stack?**
# You need the **stack** because you're **remembering nodes** while you go down left. You can't **skip the parents**, you'll need them **after** you're done with the left side.

# ---

# ---

# ## 🔥 **TL;DR (Super Simple Summary)**

# - We are **walking the tree** in **sorted order** (left → node → right).
# - Use a **stack** to **remember where we came from** as we go deep.
# - Every time we **visit a node**, we **count**.
# - When we hit **k**, we return that node's value.