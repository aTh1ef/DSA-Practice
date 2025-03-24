#neetcode35

class Solution(object):
    def exist(self, board, word):
        # first find the number of rows and columns in the board
        ROWS = len(board)
        COL = len(board[0])
        # we create a set to make sure that we do not visit the same elements again
        path = set()

        # creating a helper function
        def dfs(r, c, i):
            # if we found all the letters in the word return true
            if i == len(word):
                return True

            # now we check for conditons that are out of bound or if the conditions do not meet or the letters have already been visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COL or word[i] != board[r][c] or (r, c) in path):
                return False

            # Mark the cell as visited
            path.add((r, c))
            #  Explore all 4 directions: DOWN, UP, RIGHT, LEFT
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            # 🔙 Backtrack (undo the move)
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False

    # # 🚀 What's the Problem?

    # You have a **2D board** (a grid of letters). You have a **word**.
    # Your goal: **Can you trace the word on the board, letter by letter, moving up, down, left, or right, without reusing the same cell?**

    # Example board:
    # ```
    # [['A','B','C','E'],
    #  ['S','F','C','S'],
    #  ['A','D','E','E']]
    # ```
    # Word to find: `"ABCCED"`

    # ---

    # # 🧠 High-Level Idea

    # - You use **DFS (Depth-First Search)** to explore all possible ways you can trace out the word.
    # - You **backtrack** when you reach dead ends.
    # - Keep track of where you've been with a `path` set so you don't reuse cells.

    # ---

    # # 🔨 Step-by-Step Code Breakdown with Visualization

    # ---

    # ## 📌 **Step 1:** Initialize Rows, Cols, and Path

    # ```python
    # ROWS, COLS = len(board), len(board[0])
    # path = set()
    # ```

    # ### ➡️ Explanation
    # - `ROWS` is how many rows there are in the board (vertical).
    # - `COLS` is how many columns there are (horizontal).
    # - `path` is an empty set that will track where you've walked already.

    # ### 🧠 Layman:
    # You have a **map** (board) and you're counting how **big** it is (`ROWS` and `COLS`).
    # You're also bringing a **notepad** (`path`) to keep track of **places you've stepped** on so you don't step on the same spot twice.

    # ### 🗺️ Visualization:
    # ```
    # Board size: 3 rows x 4 columns
    # path: empty set {}
    # ```

    # ---

    # ## 📌 **Step 2:** Define the DFS Function

    # ```python
    # def dfs(r, c, i):
    # ```

    # ### ➡️ Explanation
    # - `r` and `c`: Your current row and column on the board.
    # - `i`: Index of the letter in the word you're currently trying to match.

    # ### 🧠 Layman:
    # You're a person **standing** on a letter at `(r, c)` on the board, trying to find the `i-th` letter of the word.

    # ---

    # ## 📌 **Step 3:** Base Case - Found the Whole Word!

    # ```python
    # if i == len(word):
    #     return True
    # ```

    # ### ➡️ Explanation
    # - If you've reached the **end of the word**, it means you've matched **every letter**.

    # ### 🧠 Layman:
    # "You've successfully **spelled out the word**!" 🎉
    # Time to stop and shout **SUCCESS!**

    # ### 🗺️ Visualization:
    # ```
    # WORD = "ABCCED"
    # i = 6
    # len(word) = 6
    # --> Woohoo! You found the whole word!
    # ```

    # ---

    # ## 📌 **Step 4:** Base Case - Out of Bounds or Wrong Letter or Revisit

    # ```python
    # if (r < 0 or c < 0 or
    #     r >= ROWS or c >= COLS or
    #     word[i] != board[r][c] or
    #     (r, c) in path):
    #     return False
    # ```

    # ### ➡️ Explanation
    # You're **out of bounds**, or you're standing on the **wrong letter**, or you're **stepping on the same place twice**.

    # ### 🧠 Layman:
    # 1. "Are you **off the map**? Get back!"
    # 2. "Is this **not the letter you're looking for**? Turn around!"
    # 3. "Did you **step here already**? No repeats!"

    # ### 🗺️ Visualization:
    # ```
    # Board:
    # [['A','B','C'],
    #  ['D','E','F']]
    # Word: "ABC"

    # Suppose you're at (r = -1, c = 1):
    # --> Out of bounds!

    # Or you're at (r = 1, c = 1), board[1][1] = "E"
    # But you want "B" (word[i] = "B"):
    # --> Wrong letter!

    # Or you already visited (0, 1):
    # --> Can't step here again!
    # ```

    # ---

    # ## 📌 **Step 5:** Mark the Current Cell in the Path

    # ```python
    # path.add((r, c))
    # ```

    # ### ➡️ Explanation
    # You **mark** this cell because you're standing here now.

    # ### 🧠 Layman:
    # You drop a **pebble** or **flag** to say "I've been here already!"

    # ### 🗺️ Visualization:
    # ```
    # path = {(0, 0)}
    # ```
    # You just stood on cell `(0, 0)` (maybe it's an "A").

    # ---

    # ## 📌 **Step 6:** Explore in All 4 Directions (DFS!)

    # ```python
    # res = (dfs(r + 1, c, i + 1) or
    #        dfs(r - 1, c, i + 1) or
    #        dfs(r, c + 1, i + 1) or
    #        dfs(r, c - 1, i + 1))
    # ```

    # ### ➡️ Explanation
    # Try going:
    # - Down `(r + 1)`
    # - Up `(r - 1)`
    # - Right `(c + 1)`
    # - Left `(c - 1)`
    # If **any** of these paths leads you to success (finding the word), `res` will be True.

    # ### 🧠 Layman:
    # You're at a **crossroads**.
    # You look **down the 4 roads**.
    # Try each one to see if it **leads you to the treasure** (the complete word).

    # ### 🗺️ Visualization:
    # ```
    # Current cell: (0, 0) = 'A' (1st letter of "ABC")

    # Try:
    # (1, 0): go DOWN
    # (-1, 0): go UP
    # (0, 1): go RIGHT --> "B" (2nd letter found!)
    # (0, -1): go LEFT
    # ```

    # ---

    # ## 📌 **Step 7:** Backtrack - Remove the Cell from Path

    # ```python
    # path.remove((r, c))
    # ```

    # ### ➡️ Explanation
    # Once you've explored all possibilities from this cell, you **remove** it from your path (backtrack).

    # ### 🧠 Layman:
    # You **pick up your pebble** (or flag).
    # Now someone else can **step here later**, since you're done exploring from here.

    # ### 🗺️ Visualization:
    # ```
    # path before removing = {(0, 0), (0, 1)}
    # path after removing (0, 1) = {(0, 0)}
    # ```

    # ---

    # ## 📌 **Step 8:** Return the Result of the DFS Exploration

    # ```python
    # return res
    # ```

    # ### ➡️ Explanation
    # Return True if any of the 4 moves worked, otherwise False.

    # ### 🧠 Layman:
    # "If I found the way in **any direction**, I'll tell you 'YES'.
    # If not, I'll say 'NO'."

    # ---

    # ## 📌 **Step 9:** Try Starting DFS From Every Cell on the Board

    # ```python
    # for r in range(ROWS):
    #     for c in range(COLS):
    #         if dfs(r, c, 0):
    #             return True
    # ```

    # ### ➡️ Explanation
    # You try **starting** DFS from **every cell**, to make sure you don't miss the starting point of the word.

    # ### 🧠 Layman:
    # "Start your **search** from every single square on the board.
    # Maybe the word **starts** there!"

    # ### 🗺️ Visualization:
    # ```
    # Try:
    # (0, 0): "A"
    # (0, 1): "B"
    # (0, 2): "C"
    # ...
    # ```

    # ---

    # ## 📌 **Step 10:** If You Tried Every Cell and Never Found the Word…

    # ```python
    # return False
    # ```

    # ### ➡️ Explanation
    # If you've tried everything and never found a match, return False.

    # ### 🧠 Layman:
    # "No path leads to the word.
    # Sorry, the word isn't here."

    # ---

    # ---

    # # ✅ Example Walkthrough!

    # ### Board:
    # ```
    # [['A','B','C','E'],
    #  ['S','F','C','S'],
    #  ['A','D','E','E']]
    # ```
    # ### Word: `"ABCCED"`

    # ### Steps:
    # 1. Start at `(0, 0)`: "A" ✅
    # 2. Move RIGHT to `(0, 1)`: "B" ✅
    # 3. Move DOWN to `(1, 1)`: "F" ❌ (Wrong letter!)
    #    - Backtrack to `(0, 1)`
    # 4. Move RIGHT to `(0, 2)`: "C" ✅
    # 5. Move DOWN to `(1, 2)`: "C" ✅
    # 6. Move DOWN to `(2, 2)`: "E" ✅
    # 7. Move LEFT to `(2, 1)`: "D" ✅
    # 8. Word fully matched! ✅

    # ---

    # # ⚡ Time Complexity

    # ```
    # O(n * m * 4^n)
    # ```
    # - n = number of letters in the word
    # - m = size of the board (ROWS * COLS)
    # You search from **every** cell, and explore up to **4 directions** for **n** letters.

    # ---

    # # 🎉 Final Thought for You

    # This is like **playing a maze game** on the board:
    # - You're **walking** letter by letter,
    # - You have **rules**: can't go outside, can't reuse cells, must match letters.
    # - You **explore** every possible way and **backtrack** when you hit dead ends.

