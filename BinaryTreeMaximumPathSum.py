#neetcode 33

# At first it seems like an easy problem but it really scratches your brain. You need to actually sit with a pen and paper to do this properly. I still need to redo this problem to actually get it
class Solution(object):
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            res[0] = max(res[0], root.val + leftmax + rightmax)

            return root.val + max(leftmax, rightmax)

        dfs(root)
        return res[0]

# We're solving **Maximum Path Sum in a Binary Tree**.
# The **goal**: Find the path in the tree where the sum of the **nodes' values** is the biggest.
# The path **doesn't** have to go through the root, and it must be a **continuous path**, parent-child connections only.

# ---

# ---

# ## **Code**
# ```python
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         res = [root.val]

#         def dfs(root):
#             if not root:
#                 return 0

#             leftMax = dfs(root.left)
#             rightMax = dfs(root.right)
#             leftMax = max(leftMax, 0)
#             rightMax = max(rightMax, 0)

#             res[0] = max(res[0], root.val + leftMax + rightMax)
#             return root.val + max(leftMax, rightMax)

#         dfs(root)
#         return res[0]
# ```

# ---

# ---

# # ✅ **Visualization Example Tree**
# Let's use this tree to **understand** what's happening:

# ```
#        1
#       / \
#      2   3
# ```

# ### **Values**
# - Root = 1
# - Left child = 2
# - Right child = 3

# ### **Expected Answer**
# Max path sum is **6** because `2 -> 1 -> 3` adds up to `6`.

# ---

# ---

# ## ✅ **STEP 1**:
# ```python
# res = [root.val]
# ```

# - We are storing the **result** in a **list**, because lists are **mutable** and can be updated **inside** the DFS function.
# - Initially:
#   `res = [root.val]` ➡️ root is `1`, so
#   `res = [1]`

# ---

# ---

# ## ✅ **STEP 2**: Define the DFS function
# ```python
# def dfs(root):
# ```
# - `dfs` will **walk through** every node in the tree.
# - For each node, it calculates:
#   - **What is the biggest path you can make starting from here, going down?**
#   - **What's the biggest path sum if we make a turn here (left + root + right)?**

# ---

# ---

# ## ✅ **STEP 3**: Base case
# ```python
# if not root:
#     return 0
# ```

# - If we reach a `None` node (no child), return `0` because it **adds nothing** to the path.

# ---

# ---

# ## ✅ **STEP 4**: Recurse left and right
# ```python
# leftMax = dfs(root.left)
# rightMax = dfs(root.right)
# ```

# ### Visualization:
# ```
# We start at node 1.
# dfs(root.left): we go to node 2.

# Now we're at node 2:
# - dfs(root.left): None ➡️ returns 0
# - dfs(root.right): None ➡️ returns 0

# leftMax = 0
# rightMax = 0
# ```

# ---

# ---

# ## ✅ **STEP 5**: Ignore negative paths
# ```python
# leftMax = max(leftMax, 0)
# rightMax = max(rightMax, 0)
# ```

# - We don't want **negative paths**.
# - `max(leftMax, 0)` ensures we only **keep** the path if it adds **positive value**.
# - In our tree:
#   Both are already `0` ➡️ no negative numbers.

# ---

# ---

# ## ✅ **STEP 6**: Calculate **max path sum THROUGH the current node**
# ```python
# res[0] = max(res[0], root.val + leftMax + rightMax)
# ```

# This is important!
# - You check:
#   - The **best** path **so far** (`res[0]`)
#   - OR a **new path** passing through this node:
#     ➡️ `root.val + leftMax + rightMax`

# #### Example at node 2
# - `root.val = 2`
# - `leftMax = 0`
# - `rightMax = 0`
# - Sum = `2 + 0 + 0 = 2`
# ➡️ Update `res[0] = max(1, 2) = 2`

# #### Go back to node 1 (root):
# - Now we recurse `dfs(root.right)` ➡️ node 3
# - Same as node 2 ➡️ it gives 3
# - So at root 1:
#   - `leftMax = 2`
#   - `rightMax = 3`
# - New path through node 1:
#   ➡️ `1 + 2 + 3 = 6`
# ➡️ Update `res[0] = max(2, 6) = 6`

# ---

# ---

# ## ✅ **STEP 7**: Return **one-sided path sum**
# ```python
# return root.val + max(leftMax, rightMax)
# ```

# - We return the **best path down** from this node.
# - For example:
#   - At node 2 ➡️ `2 + max(0, 0) = 2`
#   - At node 3 ➡️ `3 + max(0, 0) = 3`
#   - At node 1 ➡️ `1 + max(2, 3) = 4`
# ➡️ We **return** these to the **parent**, but note:
# `res[0]` already **saved** the **biggest full path** ➡️ `6`

# ---

# ---

# ## ✅ **STEP 8**: DFS call and return the result
# ```python
# dfs(root)
# return res[0]
# ```

# - DFS traversal is **done**
# - The result is the **maximum path sum** we've found ➡️ `6`

# ---

# ---

# ## ✅ **COMPLETE TRAVERSAL VISUALIZATION**
# ```
#        1
#       / \
#      2   3
# ```

# ### DFS(node 2)
# - left: 0
# - right: 0
# - `res = max(1, 2 + 0 + 0) = 2`
# - return `2 + max(0, 0) = 2`

# ### DFS(node 3)
# - left: 0
# - right: 0
# - `res = max(2, 3 + 0 + 0) = 3`
# - return `3 + max(0, 0) = 3`

# ### DFS(node 1)
# - left: 2
# - right: 3
# - `res = max(3, 1 + 2 + 3) = 6`
# - return `1 + max(2, 3) = 4`

# ### Final `res[0] = 6`

# ---

# ---

# # ✅ **TL;DR Recap for Our Dumbass Brain (mine too lol)**
# ### What we do:
# 1. Start DFS at root
# 2. Check both left and right children
# 3. Ignore any path that hurts us (negative)
# 4. Keep track of best "make a turn here" path (left + root + right)
# 5. Pass back best "keep going straight" path (root + max(left, right))

# ---

# ---

# ## ✅ Let's try it with a **more complex tree**

# ✔️ Negative numbers
# ✔️ Left-heavy / right-heavy paths
# ✔️ Situations where **we take a turn** at a node
# ✔️ Ignore bad paths
# ✔️ Recursion / backtracking in depth
# ✔️ Visual + side-by-side explanation

# ---

# ---

# # ✅ **Complex Example Tree**

# ```
#         -10
#         /   \
#       9      20
#             /   \
#           15     7
# ```

# ### **Node Values**
# - Root ➡️ `-10`
# - Left ➡️ `9`
# - Right ➡️ `20`
# - Right.Left ➡️ `15`
# - Right.Right ➡️ `7`

# ---

# ---

# ### **What's the Expected Answer?**
# 👉 `15 -> 20 -> 7 = 42`

# But wait, `-10 -> 20 -> 15` isn't better? Nope.
# ➡️ We'll see **why** as we go step by step.

# ---

# ---

# ## ✅ **INITIAL SETUP**

# ```python
# res = [root.val]
# ```

# 👉 `root = -10`, so
# ➡️ `res = [-10]`

# This holds our **global maximum path sum**, updated during recursion.

# ---

# ---

# # ✅ **STEP-BY-STEP DFS WITH VISUALIZATION**

# ---

# ---

# ## ✅ **STEP 1:**
# `dfs(root)` → `dfs(-10)`

# We **start** at `-10`
# - We **go left** ➡️ `dfs(9)`
# - We **go right** ➡️ `dfs(20)`

# ---

# ---

# ## ✅ **STEP 2:**
# `dfs(9)`
# - `root = 9`
# - Left ➡️ `None` ➡️ return `0`
# - Right ➡️ `None` ➡️ return `0`

# ### Now:
# ```python
# leftMax = 0
# rightMax = 0
# ```

# We **ignore** negative because of
# ```python
# leftMax = max(leftMax, 0)
# rightMax = max(rightMax, 0)
# ```

# ### Update `res`:
# ```python
# res[0] = max(res[0], 9 + 0 + 0)
#          = max(-10, 9)
#          = 9
# ```

# 👉 `res = [9]`
# Return the **one-sided path**:
# ```python
# return 9 + max(0, 0) = 9
# ```

# ---

# ---

# ## ✅ **STEP 3:**
# `dfs(20)`
# - Left ➡️ `dfs(15)`
# - Right ➡️ `dfs(7)`

# ---

# ---

# ## ✅ **STEP 4:**
# `dfs(15)`
# - Left ➡️ `None` ➡️ return `0`
# - Right ➡️ `None` ➡️ return `0`

# ### Now:
# ```python
# leftMax = 0
# rightMax = 0
# ```

# Update `res`:
# ```python
# res[0] = max(9, 15 + 0 + 0)
#          = 15
# ```

# 👉 `res = [15]`
# Return:
# ```python
# return 15 + max(0, 0) = 15
# ```

# ---

# ---

# ## ✅ **STEP 5:**
# `dfs(7)`
# - Left ➡️ `None` ➡️ return `0`
# - Right ➡️ `None` ➡️ return `0`

# ### Now:
# ```python
# leftMax = 0
# rightMax = 0
# ```

# Update `res`:
# ```python
# res[0] = max(15, 7 + 0 + 0)
#          = 15
# ```

# 👉 `res = [15]`
# Return:
# ```python
# return 7 + max(0, 0) = 7
# ```

# ---

# ---

# ## ✅ **STEP 6:**
# Back to `dfs(20)`
# - Left ➡️ `15`
# - Right ➡️ `7`

# Now:
# ```python
# leftMax = max(15, 0) = 15
# rightMax = max(7, 0) = 7
# ```

# Update `res`:
# ```python
# res[0] = max(15, 20 + 15 + 7)
#          = max(15, 42)
#          = 42
# ```

# 👉 `res = [42]`
# Return:
# ```python
# return 20 + max(15, 7) = 20 + 15 = 35
# ```

# ---

# ---

# ## ✅ **STEP 7:**
# Back to `dfs(-10)`
# - Left ➡️ `9`
# - Right ➡️ `35`

# Now:
# ```python
# leftMax = max(9, 0) = 9
# rightMax = max(35, 0) = 35
# ```

# Update `res`:
# ```python
# res[0] = max(42, -10 + 9 + 35)
#          = max(42, 34)
#          = 42
# ```

# 👉 `res = [42]`
# Return:
# ```python
# return -10 + max(9, 35) = -10 + 35 = 25
# ```

# ---

# ---

# # ✅ **FINAL STEP**
# After DFS is done:
# ```python
# return res[0]
# ```

# 👉 Return `42` 🎉

# ---

# ---

# # ✅ **WHAT HAPPENED AT EACH STEP**
# | Node | leftMax | rightMax | res[0] Updated To | Returns |
# |------|---------|----------|-------------------|---------|
# | 9    | 0       | 0        | 9                 | 9       |
# | 15   | 0       | 0        | 15                | 15      |
# | 7    | 0       | 0        | 15 (unchanged)    | 7       |
# | 20   | 15      | 7        | 42                | 35      |
# | -10  | 9       | 35       | 42 (unchanged)    | 25      |

# ---

# ---

# # ✅ **COMPLETE TREE WITH PATHS & SUMS VISUALIZED**

# ```
#         -10
#         /   \
#       9      20
#             /   \
#           15     7
# ```

# - Path: `15 -> 20 -> 7`
#   ➡️ Sum = 42 (This is our best!)

# ---

# ---

# # ✅ **Why Did It Work?**
# - **res[0]** keeps track of the **best full path sum**, even if we **turn** (left + root + right).
# - The **returned value** is the **best one-sided path** we can use when going **up** to the parent node.
# - We always ignore **negative** paths, and take **zero** if they hurt us.


# ### ✅ TL;DR:
# ➡️ `return root.val + max(leftMax, rightMax)` is **crucial** for recursion to work!
# ➡️ `return res[0]` just gives the final **answer** at the end.
# They do **different jobs**!

# ---

# ---

# ## 🔥 FULL EXPLANATION (The Dumbass-Proof Version™)

# ---

# ---

# # ✅ First, the Two Key Lines We Are Talking About:

# ```python
# return root.val + max(leftMax, rightMax)  # 🔥 THIS returns a value to the parent node!
# ```

# and
# ```python
# return res[0]  # 🔥 THIS returns the FINAL ANSWER when dfs is all done!
# ```

# ---

# ---

# # ✅ What Is `dfs()` Actually Doing?

# Think of `dfs()` like a **messenger** who:
# 1. Travels **down** the tree.
# 2. Collects the **best path sum** from the children.
# 3. Sends the **best result** **back up** to its parent.

# And **along the way**, it updates the **global best answer** in `res[0]`.

# ---

# ---

# # ✅ What Does `return root.val + max(leftMax, rightMax)` Do?

# ➡️ You are **giving your parent node** the **best one-way path sum** it can extend.
# ➡️ Why **one-way**? Because paths can't fork up the tree—
#    You can either go **left** OR **right**, not **both**, when returning to your parent.

# Imagine this:

# ```
#         10
#        /  \
#       2    10
# ```

# - When you're at node `10` (root), you ask:
#   👉 "Yo Left Child, what's your max path I can extend?"
#   👉 Left child (`2`) says: "I got a 2 for you, bro!"
#   👉 Right child (`10`) says: "I got 10 for you!"

# You pick the **biggest** one to extend: `max(2, 10) = 10`

# ➡️ So the value you return is:
# ```python
# return root.val + max(leftMax, rightMax)
# ```

# ➡️ In this case:
# ```python
# return 10 + 10 = 20
# ```

# This **"20"** is passed up to whoever called `dfs()` on this root.

# ---

# ---

# # ✅ Why Do We ALSO Update `res[0]`?

# You **also** update `res[0]` to keep track of **the best forked path**,
# aka: "What if we **don't** go back up? What if this node is the top of our path?"

# Example (at root `10`):
# You consider **both** sides at once:
# ```python
# res[0] = max(res[0], root.val + leftMax + rightMax)
# ```

# ➡️ `root.val = 10`
# ➡️ `leftMax = 2`
# ➡️ `rightMax = 10`

# So you check:
# ```python
# res[0] = max(res[0], 10 + 2 + 10) = 22
# ```

# ### 🟢 `res[0] = 22` is our **global best**,
# but the **return** to the parent is only `20` because you can't take both subtrees **up**.

# ---

# ---

# # ✅ Why Can't We Just Update `res[0]` and Forget the Return?

# Because:
# - `res[0]` holds the **global best answer**,
# - `return root.val + max(leftMax, rightMax)` feeds into the **recursive stack**
#   so the **parent** knows the **best path** it can continue from.

# If you **don't return**, the **parent call** doesn't know what to do!

# ➡️ Think of recursion like **stacked phone calls**.
# ➡️ The parent is like:
#    "Hey left child, what do you have for me?"
# ➡️ And the left child says... **nothing**, if you skip the return!
# ➡️ Then the parent can't calculate its own stuff.

# ---

# ---

# # ✅ The Two Roles
# | What           | Why It's Needed                                                                                                                                   |
# |----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
# | `res[0]`       | It keeps track of the **biggest sum of a path**, whether it's through both left & right, or just one branch. It's our **final answer**.           |
# | `return root.val + max(leftMax, rightMax)` | It gives **one side of the path** back to the parent to help **build the path sums** going up the recursion chain. It's the **return value** recursion needs! |

# ---

# ---

# # ✅ VISUAL Example!
# Tree:
# ```
#         -10
#         /  \
#        9   20
#            /  \
#          15    7
# ```

# ➡️ DFS on `15`:
# - Left & right are `None` → returns `15`
# - Updates `res[0] = max(res[0], 15) = 15`

# ➡️ DFS on `7`:
# - Left & right are `None` → returns `7`
# - Updates `res[0] = max(res[0], 7) = 15`

# ➡️ DFS on `20`:
# - Left max = 15
# - Right max = 7
# - `res[0] = max(res[0], 20 + 15 + 7) = 42`
# - Returns `20 + max(15, 7) = 35` to the parent.

# ➡️ DFS on `-10`:
# - Left max = 9
# - Right max = 35
# - `res[0] = max(res[0], -10 + 9 + 35) = 42`
# - Returns `-10 + max(9, 35) = 25` (doesn't matter anymore)

# ➡️ Finally, we return `res[0] = 42`

# ---

# ---

# # ✅ Ateef, One More Example to Cement This?

# ```
#         1
#        / \
#       2   3
# ```

# - Left path returns `2`
# - Right path returns `3`
# - `res[0] = max(res[0], 1 + 2 + 3) = 6`
# - Return `1 + max(2, 3) = 4` to the parent (which is none in this case).

# ---

# ---

# # ✅ In Your Words (For Memory)
# 👉 **Return to parent**: best path **you can extend**.
# 👉 **res[0]**: the **best path sum**, including forks, dead ends, full paths.
# 👉 You need **both**, or recursion breaks.

# ---

# ---

# # ✅ TL;DR - Is This Line Needed?
# ```python
# return root.val + max(leftMax, rightMax)
# ```
# 👉 YES! 100%
# 👉 Without it, recursion **won't work**
# 👉 You need it to **feed info back up** the call stack.