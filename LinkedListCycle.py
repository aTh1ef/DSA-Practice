#Neetcode 21
class Solution(object):
    def hasCycle(self, head):
        slow =  head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

# ### THE BIG PICTURE (What are we even doing here?)

# You have a **linked list** (think of it as a chain of nodes where each node points to the next). Sometimes, due to bad luck (or bugs), someone might mess up and make the last node point back to one of the earlier nodes. This creates a **cycle**, like a dog chasing its tail. You get stuck in an endless loop!

# Our job?
# ✅ To check if this linked list has a **cycle**.

# And to do this, we're going to use two runners:
# 🏃‍♂️ A **slow guy**
# 🏃‍♂️ A **fast guy**
# (They're called pointers, but let's imagine them as two little characters running along the linked list.)

# ---

# ---

# ## Step-By-Step Code Walkthrough (with EXPLANATIONS on every single line)

# ---

# ### First, here's the code again:

# ```python
# class Solution:
#     def hasCycle(self, head):
#         slow = head
#         fast = head

#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             if fast == slow:
#                 return True
#         return False
# ```

# ---

# ### Now, let's **zoom in** and explain **each** line like you're five:

# ---

# ---

# ## 1️⃣ `class Solution:`
# 🧠 _We're making a blueprint called `Solution`._
# ➡️ Think of it like you made a folder on your computer called "Solution" where you keep your function inside.

# ---

# ## 2️⃣ `def hasCycle(self, head):`
# 🧠 _Inside that folder (class), we have a function called `hasCycle`._
# ➡️ This is our **tool** that will look at a chain of nodes (linked list) and tell us if it has a loop or not.
# ➡️ `head` is like the **starting node** of the chain. Imagine grabbing the first link of a chain and starting from there.

# ---

# ---

# ## 3️⃣ `slow = head`
# 👟 _We're setting up the **slow runner**._
# ➡️ He starts at the first node. He's the guy who's just walking, going one node at a time.

# ---

# ## 4️⃣ `fast = head`
# 👟 _We're setting up the **fast runner**._
# ➡️ He's starting at the same place as slow, but he's going to sprint—he moves two nodes at a time.

# ---

# ### 🏃‍♂️ Visualize This:
# ```
# [1] -> [2] -> [3] -> [4] -> [5] -> None
#  ^
# Slow and Fast both start here!
# ```

# ---

# ---

# ## 5️⃣ `while fast and fast.next:`
# 👀 _As long as fast is not at the end (meaning `None`) and the next node is not `None`, we keep looping._
# ➡️ Why?
# - If fast hits the end (no cycle), then we stop.
# - If there's a cycle, fast will keep going in circles.

# ✅ This is like saying: "As long as fast can still run, keep the game going."

# ---

# ---

# ## 6️⃣ `fast = fast.next.next`
# 🏃‍♂️ _Fast guy moves **two steps** ahead._
# ➡️ He's the speedy one.
# ➡️ If there's a loop, he might catch up to slow because he's lapping him like in a race.

# ### Example (first move):
# ```
# [1] -> [2] -> [3] -> [4] -> [5] -> None
#  ^
# Slow
#            ^
#            Fast (moved 2 steps)
# ```

# ---

# ## 7️⃣ `slow = slow.next`
# 🚶‍♂️ _Slow guy moves **one step** ahead._
# ➡️ He's chill. One node at a time.
# ➡️ They're both moving at their own speeds.

# ---

# ---

# ## 8️⃣ `if fast == slow:`
# 🚨 _If fast and slow are standing on the same node… BOOM!_
# ➡️ That means there's a **cycle**, because fast lapped slow and caught him inside the loop.
# ➡️ No cycle? Fast would've sprinted to the end and hit `None`, and they'd never meet.

# ✅ So we return **True**. We found a cycle.

# ---

# ---

# ## 9️⃣ `return False` (outside the loop)
# ➡️ If fast reaches the end (no more nodes, fast is `None`),
# ➡️ They never met, no cycle here.
# ✅ So we return **False**.

# ---

# ---

# ---

# ## Visualization (Think Mario Kart 🏎️)

# Imagine this:
# You and your friend are on a racetrack (the linked list).
# - You walk (slow).
# - Your friend bikes (fast).

# ➡️ If it's a normal track (no loop), your friend bikes way ahead and leaves the track at the finish line.
# ➡️ If it's a **loop**, your friend eventually laps you, and you both end up at the same spot again!

# ---

# ---

# ## Another Visualization: "The Hamster Wheel 🐹"
# Imagine a hamster wheel.
# - Slow hamster is walking slowly.
# - Fast hamster is running fast.

# If there's **no loop**, fast hamster will eventually stop and slow hamster won't ever catch up.
# But if there **is** a loop (the wheel keeps spinning),
# ➡️ Fast hamster will **always** lap and meet the slow one somewhere!

# ---

# ---

# ## Why Two Pointers?
# 👉 The **slow pointer** explores the list steadily.
# 👉 The **fast pointer** covers ground faster.
# ➡️ If there's a cycle, **fast** catches **slow** in the loop.
# ➡️ If there's no cycle, **fast** falls off the list and hits `None`.

# ---

# ---

# ## The Magic:
# You're basically playing "tag" on a track:
# - If the track is circular (cycle), tag is inevitable!
# - If it's a straight path, the fast runner zooms off and can never tag the slow one.

# ---

# ---

# ## TL;DR (Too Long; Didn't Read)
# - `slow` = slowpoke
# - `fast` = speedster
# - If they meet, it's a **cycle**.
# - If `fast` hits the end, no cycle.

# ---

# ---

# ## Final Code with Comments (Just for You 😎)

# ```python
# class Solution:
#     def hasCycle(self, head):
#         # Both slow and fast runners start at the first node.
#         slow = head
#         fast = head

#         # As long as fast can move forward, keep going.
#         while fast and fast.next:
#             # Fast moves 2 steps.
#             fast = fast.next.next
#             # Slow moves 1 step.
#             slow = slow.next

#             # If they land on the same node, there is a loop!
#             if fast == slow:
#                 return True

#         # If fast hits the end, no loop found.
#         return False
# ```

# ---

# ---

# ## Bonus Mental Picture
# Imagine you're on a **merry-go-round**:
# - You're walking slowly.
# - Your buddy is on a bike zooming.
# ➡️ If it loops, they'll lap you.
# ➡️ If it's straight, they'll disappear.