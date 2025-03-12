#neetcode 23
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head

        # in this while loop we make sure that the right pointer is at the nth position
        while n > 0 and right:
            right = right.next
            n -= 1

        # in this pointer we move the first and second pointer by one step untill right pointer reaches null
        while right:
            left = left.next
            right = right.next

        # here we skip the nth number that we need to remove from the list
        left.next = left.next.next
        return dummy.next

# Let's break down the code step by step in very simple terms.
# I’ll show you each line, explain what it does, and even provide a little visualization to help you see what’s happening.
# Imagine you have a linked list like this:
#
# 1 -> 2 -> 3 -> 4 -> 5
#
# and you want to remove the 2nd node from the end (which is the number 4).
#
# ---
#
# ### Code with Detailed Explanations
#
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         # Create a dummy node.
#         dummy = ListNode()
#         # Connect the dummy node to the head of the list.
#         dummy.next = head
#
#         # Set up two pointers:
#         # 'left' starts at the dummy node.
#         left = dummy
#         # 'right' starts at the actual head of the list.
#         right = head
#
#         # Move the 'right' pointer forward by n steps.
#         # This creates a gap of n nodes between 'right' and 'left'.
#         while n > 0 and right:
#             right = right.next
#             n -= 1
#
#         # Move both 'left' and 'right' pointers one step at a time.
#         # When 'right' reaches the end of the list, 'left' will be
#         # just before the node that needs to be removed.
#         while right:
#             left = left.next
#             right = right.next
#
#         # Skip over the node that 'left' is pointing to next.
#         # This effectively removes that node from the list.
#         left.next = left.next.next
#
#         # Return the head of the new list.
#         return dummy.next
#
# ---
#
# ### Line-by-Line Explanation in Plain Language
#
# 1. **`class Solution:`**
#    *This line creates a class called `Solution`. In many coding challenges, you wrap your code in a class.*
#
# 2. **`def removeNthFromEnd(self, head, n):`**
#    *Here we define a function called `removeNthFromEnd` that belongs to the `Solution` class. It takes two inputs: `head` (the first node of your linked list) and `n` (which tells us which node from the end to remove).*
#
# 3. **`dummy = ListNode()`**
#    *We create a new, empty node called `dummy`. Think of this as a helper or placeholder node. It’s not part of your real list, but it helps us handle cases like deleting the first node.*
#
# 4. **`dummy.next = head`**
#    *This line attaches the dummy node to the front of your list. Now, the dummy’s "next" pointer points to the first real node (the `head`). Imagine the dummy node as a “fake” start that makes the rest of the process easier.*
#
# 5. **`left = dummy`**
#    *We set up a pointer called `left` and start it at the dummy node. A pointer is just a marker that tells us which node we're looking at.*
#
# 6. **`right = head`**
#    *Another pointer, called `right`, is set to start at the actual head of the list. Now we have two pointers: `left` (at the dummy) and `right` (at the real start).*
#
# 7. **The First `while` Loop:**
#    while n > 0 and right:
#        right = right.next
#        n -= 1
#
#    *- **Goal:** Move the `right` pointer n steps forward to create a gap between `right` and `left`.*
#    *- **How it works:** As long as `n` is greater than 0 and the `right` pointer hasn't reached the end of the list, we move `right` one step ahead and reduce `n` by 1.*
#    *- **Visualization:** If `n` is 2 and your list is `1 -> 2 -> 3 -> 4 -> 5`, then after this loop, the `right` pointer will point to `3` (two steps ahead of the start).*
#
# 8. **The Second `while` Loop:**
#    while right:
#        left = left.next
#        right = right.next
#
#    *- **Goal:** Move both pointers forward until `right` reaches the end of the list.*
#    *- **How it works:** We move `left` and `right` one step at a time together. Because `right` started out 2 nodes ahead, by the time `right` gets to the end, `left` will be just before the node we want to remove.*
#    *- **Visualization:** Continuing the example, when `right` reaches the end (`None`), `left` will be at the node with value `3`. That means the node after `left` (which is `4`) is the one we want to remove.*
#
# 9. **Skipping the Node to Remove:**
#    left.next = left.next.next
#
#    *- **Goal:** Remove the target node from the list.*
#    *- **How it works:** The `left` pointer is just before the node we want to remove. By setting `left.next` to `left.next.next`, we bypass (or “skip”) the unwanted node, linking `left` directly to the node after the removed one.*
#    *- **Visualization:** If `left` is at `3` and `left.next` is `4`, then `left.next.next` is `5`. By making `left.next` point to `5`, the node with value `4` is no longer in the chain.*
#
# 10. **`return dummy.next`**
#     *Finally, we return the new head of the list. We use `dummy.next` because `dummy` was our placeholder and the real list starts from its `next` pointer. This gives us the updated list without the removed node.*
#
# ---
#
# ### Visual Walk-Through Example
#
# Let’s say our list is:
# dummy -> 1 -> 2 -> 3 -> 4 -> 5
# and we want to remove the 2nd node from the end (node with value 4).
#
# 1. **Initialization:**
#    - `dummy` points to `1`.
#    - `left` is at `dummy`.
#    - `right` is at `1`.
#
# 2. **Moving the `right` pointer (first loop):**
#    - Move `right` 2 steps:
#      - After 1st step: `right` points to `2` (n becomes 1).
#      - After 2nd step: `right` points to `3` (n becomes 0).
#
# 3. **Moving both pointers (second loop):**
#    - Move `left` and `right` together until `right` reaches the end:
#      - 1st move:
#        - `left` goes from `dummy` to `1`.
#        - `right` goes from `3` to `4`.
#      - 2nd move:
#        - `left` goes from `1` to `2`.
#        - `right` goes from `4` to `5`.
#      - 3rd move:
#        - `left` goes from `2` to `3`.
#        - `right` goes from `5` to `None` (end of list).
#
# 4. **Remove the node:**
#    - Now `left` is at `3`, and the node to remove is `left.next` (which is `4`).
#    - We change `left.next` to point to `5` (skipping `4`).
#
# 5. **Return result:**
#    - The new list becomes: 1 -> 2 -> 3 -> 5.
#
# ---
#
# ### Summary
#
# - **Dummy Node:** Helps manage edge cases (like removing the first real node).
# - **Two Pointers:**
#   - `right` is moved ahead by n steps to create a gap.
#   - Then, moving both together ensures that when `right` is at the end, `left` is right before the target node.
# - **Removing the Node:** By redirecting `left.next` to skip the unwanted node.
# - **Return New List:** We return the list starting from the node after the dummy.
#
# I hope this step-by-step explanation makes it crystal clear!
