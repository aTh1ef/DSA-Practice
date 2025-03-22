#neetcode 29

class Solution:
    def levelOrder(self, root):

        # creating a list to store the result
        result = []

        # creating a queue for bfs
        q = collections.deque()
        q.append(root)

        while q:
            lenQ = len(q)
            level = []

            for i in range(lenQ):
                # we pop the queue from the left side
                node = q.popleft()
                # if node is not empty
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                result.append(level)

        return result

# I'm about to **teach this like you're five**.
# And we're going **deep**… like *NASA-mission-to-Mars deep*.
# Let's crack this code open, **line by line**, **visually**, and **in plain human language**, no geek talk!

# ---

# ## 🎯 What's the code about?

# It's doing a **Level Order Traversal** of a **Binary Tree**.
# Imagine you're in a building and you're **visiting floors**, **one floor at a time**, **left to right**, **top to bottom**.
# That's level order traversal.

# > TL;DR:
# You're going **floor by floor**, **row by row**.

# ---

# ## 🏢 Visualization Example of a Tree (Think of it as a building)

# ```
#         1         <- Floor 1 (Level 0)
#        / \
#       2   3      <- Floor 2 (Level 1)
#      / \   \
#     4   5   6   <- Floor 3 (Level 2)
# ```

# If you **traverse floor by floor**, it looks like:
# ```
# [ [1], [2, 3], [4, 5, 6] ]
# ```

# ---

# ## 🔧 Now let's BREAK DOWN the CODE LINE BY LINE
# And **visualize** where your brain should be at every step.

# ---

# ---

# ## 📜 Code - The Top Part
# ```python
# class Solution:
# ```
# 🧠 Think of this as **creating a box** that will hold our solution.
# It's like **naming a recipe**.

# ---

# ```python
# def levelOrder(self, root: TreeNode) -> List[List[int]]:
# ```

# ### What does this do?
# 🗣️ _"Hey! I'm making a **function** called `levelOrder` that will give me **levels** in a tree, one by one."_
# You give me a **tree** (`root`), and I give you **lists of lists** of numbers, each representing one **floor** in the tree.

# ---

# ```python
# res = []
# ```
# - `res` is where we'll **store** the answer.
# - Picture `res` like your **notebook** where you're writing down **who lives on each floor** of the building.

# ---

# ---

# ## 🪣 Make a Queue!
# ```python
# q = collections.deque()
# ```
# - This is a **queue**, like people **lining up** at a counter.
# - **First in, first out (FIFO)**.
# Think of **waiting in line at KFC**, whoever comes first gets served first.

# ---

# ```python
# q.append(root)
# ```
# - We **put the root** (the big boss node at the top of the tree) **into the line**.
# - 🧠 Imagine you **open the building door**, and the **first person** you meet is **Node 1 (root)**.

# ---

# ---

# ## 🏃 Walk the Building, Floor by Floor!
# ```python
# while q:
# ```
# 🗣️ _"As long as there are people in the queue (someone to visit), keep going!"_

# At this point, we are **standing in front of the building**
# - We'll **visit each floor**,
# - Check who's there
# - Then **add their children** (if any) to the **queue** for the **next visit**.

# ---

# ---

# ## 🔢 Get the number of people on this floor
# ```python
# qLen = len(q)
# ```
# - This tells us **how many people** are currently in line.
# - **These are the people on this floor!**
# 🧠 Example:
# - You come to Floor 1
# - You see **only 1 person in line**, that's Node `1`.
# `qLen = 1`

# ---

# ---

# ## 🗒️ Start a list for this level!
# ```python
# level = []
# ```
# - This list will hold **all the people you meet** on **this floor**.
# - Picture it like writing **everyone's name** on this floor in your **notebook page**.

# ---

# ---

# ## 🚶‍♂️ Visit Everyone on This Level
# ```python
# for i in range(qLen):
# ```
# - You're saying **"For everyone on this floor, do this..."**
# - We loop through **everyone on this level**
# - Example:
#   `qLen = 2` → you loop **two times** for people on this floor.

# ---

# ---

# ## 👋 Meet the next person in line
# ```python
# node = q.popleft()
# ```
# - You **take the first person out** of the queue.
# - FIFO: **First person who entered, gets served first**.

# Example:
# - Queue was `[1]`
# - `node = 1`
# Now `q` is empty until we **add children** later.

# ---

# ---

# ## 🗨️ If there's actually someone there
# ```python
# if node:
# ```
# - Double-check you actually got a **real node** and not a **ghost (None)**.

# ---

# ---

# ## ✍️ Write down their name!
# ```python
# level.append(node.val)
# ```
# - You **write the node's value** down on your **list for this level**.

# Visualization:
# - You met `node = 1`
# - You write down `1` in the level list.
# `level = [1]`

# ---

# ---

# ## 👶 Add their kids to the next floor queue!
# ```python
# q.append(node.left)
# q.append(node.right)
# ```
# - You check if this person has **kids (left and right)**
# - If they do, you **add them to the queue**
# - You'll **visit them** on the **next loop**, i.e., next floor.

# Example:
# - Node `1` has kids: `2` and `3`
# - `q` becomes `[2, 3]`
# 🧠 **Next time** we go back to `while q`, we're meeting `2` and `3`.

# ---

# ---

# ## 🏗️ After visiting everyone on the floor, save the level!
# ```python
# if level:
#     res.append(level)
# ```
# - After you finish **everyone on this floor**,
# - You **add the list** to your **notebook (`res`)**

# Example:
# - `level = [1]`
# - Now `res = [[1]]`

# ---

# ---

# ## 🏁 Done! Return the notebook
# ```python
# return res
# ```
# - Return your **list of lists**
# - This shows **who's on each floor**, in order.

# ---

# ---

# ---

# ## 🏢 Real-Life Visualization Example
# ### Given this tree:
# ```
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
# ```

# - Start at root `1`
# - Queue = `[1]`
# ---
# ### First while loop:
# - qLen = 1
# - level = []
# - Visit `1`
# - Add `1` to level → `[1]`
# - Add `2` and `3` to queue
# - Queue = `[2, 3]`
# - Add level `[1]` to res
# - res = `[[1]]`

# ---
# ### Second while loop:
# - qLen = 2
# - level = []
# - Visit `2`
# - Add `2` to level → `[2]`
# - Add `4` and `5` to queue
# - Queue = `[3, 4, 5]`
# - Visit `3`
# - Add `3` to level → `[2, 3]`
# - Add `6` to queue
# - Queue = `[4, 5, 6]`
# - Add level `[2, 3]` to res
# - res = `[[1], [2, 3]]`

# ---
# ### Third while loop:
# - qLen = 3
# - level = []
# - Visit `4`
# - Add `4` to level → `[4]`
# - No kids → don't add anything
# - Visit `5`
# - Add `5` to level → `[4, 5]`
# - No kids
# - Visit `6`
# - Add `6` to level → `[4, 5, 6]`
# - No kids
# - Queue is empty
# - Add level `[4, 5, 6]` to res
# - res = `[[1], [2, 3], [4, 5, 6]]`

# ---

# ---

# ---

# ## ✅ Full Code Again for Context
# ```python
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res = []                           # Notebook to store levels

#         q = collections.deque()            # Our line (queue)
#         q.append(root)                     # Start with the root

#         while q:                           # While there are people in line
#             qLen = len(q)                  # How many on this floor?
#             level = []                     # New page in notebook

#             for i in range(qLen):          # Visit everyone on this floor
#                 node = q.popleft()         # Meet the next person
#                 if node:                   # If they exist
#                     level.append(node.val) # Write their name
#                     q.append(node.left)    # Add their left child
#                     q.append(node.right)   # Add their right child

#             if level:                      # Finished this floor
#                 res.append(level)          # Save it to notebook

#         return res                         # Give me the notebook!
# ```

# ---

# ---

# ## 🧠 Mental Model to Remember
# - **Queue** is like **people waiting in line**
# - Each **while loop** is a **floor visit**
# - `qLen` tells you how many **rooms** on the **current floor**
# - `level` is your **guest list** for this floor
# - `res` is your **full guest log**, floor by floor