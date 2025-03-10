#neetcode 19
class Solution:
    def reverseList(self, head):
        prev, current = None, head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

# Let's break down the linked list reversal code **line by line** in the simplest way possible. I'll also explain what a linked list is using analogies and then go through each line of the code, so you can visualize exactly what's happening. Think of this as a step-by-step guide for someone who's new to this.

# ---

# ## What Is a Linked List?

# Imagine a linked list as a **chain of paper clips**.
# - **Each paper clip is a node.**
# - Every node holds some **data** (in our case, a value) and a **pointer** (or "link") to the **next node** in the chain.
# - The first node is called the **head**, and it points to the next node.
# - The very last node points to nothing (in Python, we use `None` for that).

# ### In Python:

# You might see it defined like this:
# ```python
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val   # This is the data held by the node.
# #         self.next = next # This is a pointer to the next node.
# ```

# ---

# ## The Code for Reversing a Linked List

# Here's the code we're going to explain:
# ```python
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev, curr = None, head

#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         return prev
# ```

# ---

# ## Line-by-Line Explanation

# ### **Line 1: Class Definition**
# ```python
# class Solution:
# ```
# - **What it does:**
#   It creates a container (a class) called `Solution` where we keep our functions.
# - **Layman's terms:**
#   Think of it like a toolbox. All your tools (functions) are kept here.

# ---

# ### **Line 2: Function Definition**
# ```python
#     def reverseList(self, head: ListNode) -> ListNode:
# ```
# - **What it does:**
#   This line defines a function named `reverseList` that takes one parameter `head`, which is the starting node (or "head") of your linked list. It will return the new head of the reversed list.
# - **Layman's terms:**
#   You're saying, "Hey, here's a recipe to flip my chain of paper clips. I give you the first paper clip, and you'll return the first paper clip of the reversed chain."

# ---

# ### **Line 3: Initializing Pointers**
# ```python
#         prev, curr = None, head
# ```
# - **What it does:**
#   Two pointers are set up:
#   - `prev` is initialized to `None` because there is no previous node before the head.
#   - `curr` is set to the head of the list (the starting node).
# - **Layman's terms:**
#   Imagine you're holding a chain of paper clips.
#   - `curr` is the paper clip you're currently holding (starting with the first one).
#   - `prev` is the one you just came from (nothing yet, so it's `None`).

# ---

# ### **Line 4: The While Loop**
# ```python
#         while curr:
# ```
# - **What it does:**
#   This loop continues as long as `curr` is not `None`. In other words, while there are still nodes to process.
# - **Layman's terms:**
#   "Keep flipping the chain until there are no more paper clips left to handle."

# ---

# ### **Line 5: Store the Next Node**
# ```python
#             temp = curr.next
# ```
# - **What it does:**
#   It saves the next node in a temporary variable `temp`. This is necessary because once you reverse the pointer, you lose the original link to the rest of the list.
# - **Layman's terms:**
#   Before you disconnect the current paper clip from the chain, you write down the name (or note) of the next paper clip so you remember where to go next.

# ---

# ### **Line 6: Reverse the Pointer**
# ```python
#             curr.next = prev
# ```
# - **What it does:**
#   It reverses the link of the current node (`curr`). Instead of pointing to the next node, it now points back to `prev`.
# - **Layman's terms:**
#   You take the current paper clip and make it point backwards to the one you already processed. It's like turning the chain around so each clip now points to the previous one instead of the next.

# ---

# ### **Line 7: Move `prev` Forward**
# ```python
#             prev = curr
# ```
# - **What it does:**
#   Now, update `prev` to be the current node because it's now the last processed node.
# - **Layman's terms:**
#   After flipping a paper clip, you move your "memory" of the previous clip forward. Now, the current paper clip becomes your new "previous" clip.

# ---

# ### **Line 8: Move `curr` Forward**
# ```python
#             curr = temp
# ```
# - **What it does:**
#   Move to the next node by setting `curr` to the node stored in `temp`.
# - **Layman's terms:**
#   You pick up the next paper clip (the one you noted earlier) and hold it in your hand. Now you're ready to process this one next.

# ---

# ### **Line 9: Return the New Head**
# ```python
#         return prev
# ```
# - **What it does:**
#   Once the loop is finished (i.e., `curr` becomes `None` meaning you've reached the end), `prev` will be pointing to the new head of the reversed list.
# - **Layman's terms:**
#   After all paper clips have been flipped, `prev` holds the first paper clip of the now reversed chain. You give that back as the final result.

# ---

# ## Visualizing the Process

# ### Imagine Your Linked List as:
# ```
# Head -> [1] -> [2] -> [3] -> [4] -> None
# ```

# ### **Step-by-Step:**

# 1. **Initial Setup:**
#    - `prev = None`
#    - `curr = [1]`

# 2. **First Iteration:**
#    - `temp = [2]` (save next node)
#    - Reverse pointer: Make `[1].next = None` (since `prev` is `None`)
#    - Move `prev` to `[1]`
#    - Move `curr` to `[2]`
#
#    Now list is split:
#    - Reversed part: `[1] -> None`
#    - Remaining: `[2] -> [3] -> [4] -> None`

# 3. **Second Iteration:**
#    - `temp = [3]`
#    - Reverse pointer: Make `[2].next = [1]` (linking back to `[1]`)
#    - Move `prev` to `[2]`
#    - Move `curr` to `[3]`
#
#    Reversed part now: `[2] -> [1] -> None`
#    Remaining: `[3] -> [4] -> None`

# 4. **Third Iteration:**
#    - `temp = [4]`
#    - Reverse pointer: Make `[3].next = [2]`
#    - Move `prev` to `[3]`
#    - Move `curr` to `[4]`
#
#    Reversed part now: `[3] -> [2] -> [1] -> None`
#    Remaining: `[4] -> None`

# 5. **Fourth Iteration:**
#    - `temp = None` (since `[4].next` is `None`)
#    - Reverse pointer: Make `[4].next = [3]`
#    - Move `prev` to `[4]`
#    - Move `curr` to `None`
#
#    Final reversed list: `[4] -> [3] -> [2] -> [1] -> None`

# 6. **Return `prev`:**
#    `prev` now points to `[4]`, which is the new head.

# ---

# ## Summary in Super-Layman Terms

# - **Linked List:** Think of it like a chain of paper clips. Each clip (node) knows which clip comes next.
# - **Reversing the List:** You're flipping the chain so that every clip now points to the one before it instead of the one after it.
# - **Pointers (`prev` and `curr`):**
#   - `curr` is the paper clip you're currently flipping.
#   - `prev` is the chain of clips you've already flipped.
# - **Process:**
#   1. Save the next clip (`temp`).
#   2. Flip the current clip so it points backward.
#   3. Move your "flipped chain" pointer (`prev`) to include the current clip.
#   4. Move to the next clip.
# - **End Result:** Once you run out of clips (nodes), `prev` holds the new starting clip of the reversed chain.

# ---

# This detailed, line-by-line explanation should help you see not only **what** the code is doing but also **why** it does it that way. If you need any more clarifications or another analogy, just let me know!
