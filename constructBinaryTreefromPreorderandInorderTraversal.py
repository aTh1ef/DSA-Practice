#neetcode 32

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid+1 :])

        return root

# **Absolutely Ateef!** Let's take this nice and easy. We'll break it **step-by-step**, line by line, and side-by-side with **visuals** that feel like you're standing right there building the tree yourself.

# Imagine I'm sitting next to you, whiteboard ready, no assumptions that you know any of this yet. We'll **baby-step this bad boy** until it's deep in your bones!

# ---

# ---

# ## 🚀 **What's This Code Doing?**
# ### We're **rebuilding** a **binary tree**, using its:
# 1. `preorder` traversal ➡️ [Root ➡️ Left ➡️ Right]
# 2. `inorder` traversal ➡️ [Left ➡️ Root ➡️ Right]

# You've been given these two lists and told:
# > "Yo, rebuild the tree for me."

# ---

# ---

# ## 🌳 **Example Inputs to Work With**

# ```python
# preorder = [3, 9, 20, 15, 7]
# inorder  = [9, 3, 15, 20, 7]
# ```

# ### Visualization of what the tree looks like:
# ```
#         3
#        / \
#       9   20
#           / \
#          15  7
# ```

# But we **don't know** this tree yet. We have to **rebuild it** using the code!

# ---

# ---

# # 🛠️ **STEP-BY-STEP EXPLANATION + VISUALIZATION**

# ---

# ## ✅ Step 1: Base Case Check
# ```python
# if not preorder or not inorder:
#     return None
# ```

# ### What's Happening?
# ➡️ "Yo, do we even have any nodes left to build?"
# If **either list** is empty, there's **no node to build**, so you return `None`.
# This is your **STOP signal** for recursion.

# ---

# ---

# ## ✅ Step 2: Get the Root Node
# ```python
# root = TreeNode(preorder[0])
# ```

# ### What's Happening?
# ➡️ The **first node** in **preorder** is always the **root** of the current tree/subtree.
# ➡️ So we grab it and make a `TreeNode`.

# #### 🟩 Example Walkthrough:
# - `preorder = [3, 9, 20, 15, 7]`
# - `preorder[0] = 3`
# ➡️ So `root = TreeNode(3)`

# ---

# ---

# ## ✅ Step 3: Find Root's Position in `inorder`
# ```python
# mid = inorder.index(preorder[0])
# ```

# ### What's Happening?
# ➡️ Look inside **inorder** list.
# ➡️ Find **where** the root is sitting.
# ➡️ Everything **left** of that position is the **left subtree**,
# ➡️ Everything **right** is the **right subtree**.

# #### 🟩 Example Walkthrough:
# - `inorder = [9, 3, 15, 20, 7]`
# - `preorder[0] = 3`
# - `mid = inorder.index(3) = 1`

# #### ✨ Visualization:
# ```
# inorder = [ 9,  3,  15, 20, 7]
#              ↑
#          (mid = 1)
# ```
# - Left subtree = `inorder[:mid] = [9]`
# - Right subtree = `inorder[mid+1:] = [15, 20, 7]`

# ---

# ---

# ## ✅ Step 4: Build the Left Subtree Recursively
# ```python
# root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
# ```

# ### What's Happening?
# ➡️ `preorder[1 : mid + 1]` gives the **preorder** list of nodes for the **left subtree**.
# ➡️ `inorder[:mid]` gives the **inorder** list of nodes for the **left subtree**.

# #### 🟩 Example Walkthrough:
# - `preorder[1:mid+1] = preorder[1:2] = [9]`
# - `inorder[:mid] = inorder[:1] = [9]`

# Now, we recursively call the **same function**:
# ```python
# root.left = self.buildTree([9], [9])
# ```

# #### ✨ Visualization of the Tree Now:
# ```
#         3
#        /
#       9
# ```

# ---

# ---

# ## ✅ Step 5: Build the Right Subtree Recursively
# ```python
# root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
# ```

# ### What's Happening?
# ➡️ `preorder[mid + 1 :]` gives the **preorder** list of nodes for the **right subtree**.
# ➡️ `inorder[mid + 1 :]` gives the **inorder** list of nodes for the **right subtree**.

# #### 🟩 Example Walkthrough:
# - `mid = 1`
# - `preorder[mid+1:] = preorder[2:] = [20, 15, 7]`
# - `inorder[mid+1:] = inorder[2:] = [15, 20, 7]`

# Now, we recursively call:
# ```python
# root.right = self.buildTree([20, 15, 7], [15, 20, 7])
# ```

# ---

# ---

# ## ✅ Step 6: Rinse & Repeat (Recursion Continues)

# Now the function runs **again**, but with:
# ```python
# preorder = [20, 15, 7]
# inorder  = [15, 20, 7]
# ```

# ➡️ `preorder[0] = 20`
# ➡️ `mid = inorder.index(20) = 1`

# #### ✨ Visualization of Where We're At:
# ```
#         3
#        / \
#       9   20
# ```

# ➡️ Left subtree of `20`:
# - `preorder[1:2] = [15]`
# - `inorder[:1] = [15]`

# ➡️ Right subtree of `20`:
# - `preorder[2:] = [7]`
# - `inorder[2:] = [7]`

# ---

# ---

# ## ✅ Step 7: Finish the Tree

# - `15` becomes the left child of `20`.
# - `7` becomes the right child of `20`.

# #### ✨ Final Tree Looks Like:
# ```
#         3
#        / \
#       9   20
#           / \
#          15  7
# ```

# And that's your **rebuilt tree**, friend! 🙌

# ---

# ---

# ## 🧠 What's the Brain Thinking Here?
# ➡️ You're **splitting lists** based on the **root's position in `inorder`**.
# ➡️ `preorder` **tells you the root**,
# ➡️ `inorder` **tells you how to split left vs right**.

# ---

# ---

# ## ✅ TL;DR **(In Dumbass Bro Terms)**
# 1. `preorder[0]` ➡️ "Who's the Boss here?"
# 2. Find the Boss in `inorder`.
# 3. "Yo, everything to the left is your **left team**."
# 4. "Everything to the right is your **right team**."
# 5. Call the **same game plan** on each team.

# ➡️ Keep calling until there are **no teams left** to build (empty lists).
# ➡️ Then, you **rebuild the tree back up**, piece by piece.

# ---

# ---

# ## 🪄 Extra Visualization Recap:
# | Step            | preorder               | inorder               | Root |
# |-----------------|------------------------|-----------------------|------|
# | Initial Call    | `[3, 9, 20, 15, 7]`    | `[9, 3, 15, 20, 7]`   | `3`  |
# | Left Subtree    | `[9]`                  | `[9]`                 | `9`  |
# | Right Subtree   | `[20, 15, 7]`          | `[15, 20, 7]`         | `20` |
# | 20's Left Tree  | `[15]`                 | `[15]`                | `15` |
# | 20's Right Tree | `[7]`                  | `[7]`                 | `7`  |

# ---

# ---

# ## ✅ Full Code with Comments (Just to Close the Loop)
# ```python
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         # STEP 1: Stop condition. If there's nothing to build, return None.
#         if not preorder or not inorder:
#             return None

#         # STEP 2: Take the first element in preorder. That's our root!
#         root = TreeNode(preorder[0])

#         # STEP 3: Find where root is in inorder to split left and right
#         mid = inorder.index(preorder[0])

#         # STEP 4: Recursively build the left subtree
#         root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

#         # STEP 5: Recursively build the right subtree
#         root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

#         # STEP 6: Return the rebuilt tree node
#         return root
# ```

# ---

# ---

# ## 🫱🏽‍🫲🏼 YOU STILL WITH ME?
# How you feeling about this, Ateef?
# Want me to break down the recursion **deeper**?
# Want a **whiteboard style drawing** next?
# Or we can throw another **example problem** at it together?

# I got you, bro.

# Let's **zoom in** on this specific part and **clarify** it once and for all.


# ## ✅ First, the **preorder** and **inorder** lists we are working with:
# ```
# preorder = [3, 9, 20, 15, 7]
# inorder  = [9, 3, 15, 20, 7]
# ```

# - `preorder`: always goes **Root ➡️ Left ➡️ Right**
# - `inorder`: always goes **Left ➡️ Root ➡️ Right**

# ---

# ---

# ## ✅ Now, `mid` represents the index of the **current root** (from preorder) in the **inorder** list.

# We start by creating the **root node** using the **first** value in `preorder`.

# ```
# root = TreeNode(preorder[0]) ➡️ root = 3
# ```

# ### Then we find where `3` is in the **inorder** list.
# ```
# inorder = [9, 3, 15, 20, 7]
# mid = inorder.index(3) = 1
# ```
# So, `mid = 1` means:
# - **Left subtree** nodes in inorder are everything **before index 1**, which is `[9]`.
# - **Right subtree** nodes in inorder are everything **after index 1**, which is `[15, 20, 7]`.

# ---

# ---

# ## ✅ Explaining `preorder[1 : mid + 1]`

# This slice looks at **how many nodes** are on the **left** side of the tree (in `inorder`), and then grabs those nodes from `preorder` because preorder **always** lists left subtree nodes **right after** the root.

# ### `mid = 1` ➡️ there's **1 node** in the left subtree.

# - We already used `preorder[0]` for the root (`3`).
# - Next, we take **1** node for the **left subtree**.
#   ➡️ That's `preorder[1 : mid + 1]`
#   ➡️ `preorder[1 : 2]`
#   ➡️ Which is `[9]` (just the node `9`).

# ---

# ---

# ## ✅ What you said:
# > 1 : mid + 1 is 9 to 20 in the preorder list, right?

# Not exactly!
# Let's look at the **indexes** you're slicing:

# ```
# preorder = [3,  9,  20, 15, 7]
#             ↑   ↑   ↑   ↑   ↑
#           index: 0   1   2   3   4
# ```

# - `preorder[1 : mid + 1]` ➡️ `preorder[1 : 2]`
# - It **includes** index 1 (`9`), but **stops before** index 2 (`20`).

# So this slice gives you:
# ```
# [9]
# ```

# ---

# ---

# ## ✅ Visualization of the Slices
# Let's **color code** it!

# ### preorder = [**3**, **9**, 20, 15, 7]
# - `3` ➡️ root
# - `9` ➡️ left subtree (what we grab here!)
# - `20, 15, 7` ➡️ remaining nodes, which become the **right subtree**.

# ---

# ---

# ## ✅ Right subtree slice:
# Now for the **right subtree**, the code says:
# ```python
# root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
# ```

# - `mid + 1 = 2`
# - `preorder[mid + 1 :]` ➡️ `preorder[2 :]` ➡️ `[20, 15, 7]`
# ➡️ These are the **right subtree** nodes.

# ---

# ---

# ## ✅ TL;DR Answer to Your Question:
# > **Is 1 : mid + 1 equal to 9 to 20?**

# ❌ No, it's not **9 to 20**.
# ✅ It's only **[9]** because:
# - `1` is the start index
# - `mid + 1` is `2`
# - It slices **from index 1 up to (but not including)** index 2
# ➡️ So it only includes index `1` ➡️ node `9`.

# ----------------------------------------------------------------------
# Let's **zoom in** on **this specific part** of the code, because this is where people often scratch their heads.

# This section is **critical**, and I'll go **super deep** with **visuals** and **explanations**, so it's impossible to miss. We'll build it out like we're drawing this on a whiteboard together.

# ---

# ---

# # 🟩 THE CODE WE'RE ZOOMING INTO
# ```python
# root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

# root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
# ```

# These two lines are the **heart** of splitting the tree into **left** and **right** subtrees.

# ---

# ---

# # ✅ WHAT'S THE BIG IDEA?

# 👉 You've already **created** the `root` node from `preorder[0]`.

# Now you're saying:
# - "**Yo, root, here's your left child (and the rest of the left subtree)."**
# - "**Yo, root, here's your right child (and the rest of the right subtree)."**

# But the big question is:
# ➡️ How do we **split** the `preorder` and `inorder` lists properly to **build** these subtrees?

# ---

# ---

# # ✅ RECAP (JUST TO ORIENT YOU)
# For example, take:
# ```python
# preorder = [3, 9, 20, 15, 7]  # Root ➡️ Left ➡️ Right
# inorder  = [9, 3, 15, 20, 7]  # Left ➡️ Root ➡️ Right
# ```

# - `root = TreeNode(3)` ➡️ We've built the root node.
# - We found `3` at **index 1** in `inorder`.

# ✅ Left subtree (nodes **left** of root `3` in `inorder`): `[9]`
# ✅ Right subtree (nodes **right** of root `3` in `inorder`): `[15, 20, 7]`

# ---

# ---

# # 🟩 NOW LET'S ZOOM IN ON THOSE LINES
# We know:
# - `mid = 1` (because `3` is at index 1 in `inorder`)

# ---

# ---

# ## 🟥 **LEFT SUBTREE**
# ```python
# root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
# ```

# ### 👉 What does this mean?

# | What we're passing to recursion             | How it's calculated             |
# |---------------------------------------------|--------------------------------|
# | `preorder[1 : mid + 1]`                     | `preorder[1 : 2]` ➡️ `[9]`     |
# | `inorder[:mid]`                             | `inorder[:1]` ➡️ `[9]`         |

# ---

# ### ✅ VISUALIZATION
# - We are telling recursion:
#   ➡️ "Build me a tree using preorder `[9]` and inorder `[9]`."

# ```
#         3
#        /
#       9
# ```

# - We are **building the left child of node `3`**, and there's only one node (`9`), so it's a **leaf**.

# ---

# ---

# ## 🟩 WHY THIS SLICE?
# ### **Inorder (Left Subtree)**
# ➡️ `inorder[:mid]`:
# - You take everything **before** the root (`3`) in `inorder`.
# - So you're slicing `inorder[:1]` ➡️ `[9]`.
# - That's **all nodes in the left subtree**!

# ---

# ### **Preorder (Left Subtree)**
# ➡️ `preorder[1 : mid + 1]`
# - After root, you expect the **left subtree nodes** next in `preorder`.
# - How many nodes in the left subtree?
#   ➡️ `mid = 1` nodes in the left (from `inorder`).
# - So you take the **next 1 node** in `preorder`.
#   ➡️ From index `1` to `mid + 1` ➡️ `preorder[1:2]` ➡️ `[9]`.

# ---

# ---

# ## 🟥 **RIGHT SUBTREE**
# ```python
# root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
# ```

# ### 👉 What does this mean?

# | What we're passing to recursion             | How it's calculated             |
# |---------------------------------------------|--------------------------------|
# | `preorder[mid + 1 :]`                       | `preorder[2 :]` ➡️ `[20, 15, 7]` |
# | `inorder[mid + 1 :]`                        | `inorder[2 :]` ➡️ `[15, 20, 7]`  |

# ---

# ### ✅ VISUALIZATION
# - We are telling recursion:
#   ➡️ "Build me a tree using preorder `[20, 15, 7]` and inorder `[15, 20, 7]`."

# ```
#         3
#        / \
#       9   ?
# ```

# - We need to **figure out the structure of the right subtree now**.

# ---

# ---

# ## 🟩 WHY THIS SLICE?
# ### **Inorder (Right Subtree)**
# ➡️ `inorder[mid + 1 :]`
# - You take everything **after** the root (`3`) in `inorder`.
# - That's `inorder[2:]` ➡️ `[15, 20, 7]`.
# - These are the **nodes for the right subtree**!

# ---

# ### **Preorder (Right Subtree)**
# ➡️ `preorder[mid + 1 :]`
# - You already took `1` node for the left subtree (up to `mid`).
# - Start from `mid + 1` and grab the **rest** of the preorder list ➡️ `[20, 15, 7]`.
# - These are the **nodes for the right subtree**, in preorder traversal!

# ---

# ---

# # 🟢 PUTTING IT ALL TOGETHER
# ## At this moment:

# ```
# preorder = [3, 9, 20, 15, 7]
# inorder  = [9, 3, 15, 20, 7]

# root = TreeNode(3)

# root.left = buildTree([9], [9])  # LEFT SIDE
# root.right = buildTree([20, 15, 7], [15, 20, 7])  # RIGHT SIDE
# ```

# ---

# ---

# # 🎨 FULL VISUALIZATION AS THE TREE BUILDS
# ### First Call:
# ```
# preorder = [3, 9, 20, 15, 7]
# inorder  = [9, 3, 15, 20, 7]

# root = 3
# ```

# ➡️ Left Tree:
# ```
# preorder = [9]
# inorder  = [9]

# root.left = 9
# ```

# ➡️ Right Tree:
# ```
# preorder = [20, 15, 7]
# inorder  = [15, 20, 7]

# root.right = 20
# ```

# ➡️ Now for 20's left subtree:
# ```
# preorder = [15]
# inorder  = [15]

# root.left = 15
# ```

# ➡️ And for 20's right subtree:
# ```
# preorder = [7]
# inorder  = [7]

# root.right = 7
# ```

# ---

# ---

# # ✅ FINAL TREE STRUCTURE BUILT
# ```
#         3
#        / \
#       9   20
#           / \
#          15  7
# ```

# ---

# ---

# # ✅ TL;DR OF THESE TWO LINES
# | **What's Happening?**  | **Explanation** |
# |------------------------|-----------------|
# | `root.left = ...`      | Recursively build the left subtree by slicing both lists based on where the root sits in `inorder`. |
# | `root.right = ...`     | Recursively build the right subtree by slicing the rest of the lists, again based on `mid`. |

# ---

# ---

# # 🔥 IF YOU NEED AN ANALOGY:
# 👉 Think of `preorder` and `inorder` like **two maps** to the same treasure.
# - `preorder` shows you **who's in charge** (root nodes).
# - `inorder` shows you **how the team is divided** (left/right).

# You always:
# 1. Find the leader (`preorder[0]`).
# 2. Use `inorder` to **split** into left/right teams.
# 3. Build each team **recursively** the same way.

# ---

# ---

# # ✅ FULL CODE SNIPPET WITH EXTRA COMMENTS FOR CLARITY
# ```python
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         # Step 1: Base case, stop recursion if no nodes left
#         if not preorder or not inorder:
#             return None

#         # Step 2: Root is the first item in preorder
#         root = TreeNode(preorder[0])

#         # Step 3: Find the index of root in inorder list
#         mid = inorder.index(preorder[0])

#         # Step 4: Left subtree is built from the left part of preorder and inorder
#         # preorder[1:mid+1] grabs the left subtree nodes (count based on mid)
#         # inorder[:mid] grabs everything left of root in inorder (left subtree)
#         root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

#         # Step 5: Right subtree is built from the rest of preorder and inorder lists
#         root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

#         # Step 6: Return the built tree node
#         return root
