# Given a string s, write a function that finds and returns the longest palindromic substring in s.
# A palindrome is a string that reads the same forward and backward.
# You must use the "expand around center" technique to check both odd-length (single center)
# and even-length (double center) palindromes.
class Solution:
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        longest = ""

        for i in range(len(s)):
            oddPalindrome = expandAroundCenter(i, i)
            evenPalindrome = expandAroundCenter(i, i + 1)

            longest = max(longest, oddPalindrome, evenPalindrome, key=len)

        return longest


if __name__ == "__main__":
    s = "abba"
    sol = Solution()
    answer = sol.longestPalindrome(s)
    print(answer)

    """
    # Understanding the Expand-Around-Center Algorithm for Longest Palindromic Substring

    ---

    ## 1. Problem Overview

    **Goal:**  
    Given a string `s`, find the longest substring that is a palindrome (i.e., reads the same forward and backward).

    **Example Inputs and Outputs:**

    - **Input:** "babad"  
      **Output:** "bab" or "aba"
    - **Input:** "cbbd"  
      **Output:** "bb"

    ---

    ## 2. The Key Idea: Expanding Around a Center

    Every palindrome is symmetric around its center. This allows us to:
    - **Directly "jump" to a potential center** in the string.
    - **Expand outward** from that center while the characters match.
    - **Handle both odd-length and even-length palindromes.**

    ### Detecting the Center

    There are two types of centers:
    - **Odd-Length Palindrome:**  
      Treat a single character as the center.  
      Example call in code:
      odd_pal = expandAroundCenter(i, i)
      (Both left and right pointers start at the same index `i`.)

    - **Even-Length Palindrome:**  
      The center lies between two characters.  
      Example call in code:
      even_pal = expandAroundCenter(i, i + 1)
      (Here, the left pointer is at `i` and the right pointer at `i + 1`.)

    These calls are what “jump” directly to the center of every possible palindromic substring.

    ---

    ## 3. The Code

    Below is the complete solution using a helper function `expandAroundCenter`:

    class Solution:
        def longestPalindrome(self, s: str) -> str:
            def expandAroundCenter(left, right):
                # Expand while the substring is a palindrome.
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1  # Move left pointer one step to the left.
                    right += 1  # Move right pointer one step to the right.
                # Return the valid palindromic substring.
                return s[left + 1:right]

            longest = ""
            for i in range(len(s)):  # Check each index as a potential center.
                odd_pal = expandAroundCenter(i, i)      # Odd-length palindrome.
                even_pal = expandAroundCenter(i, i + 1)   # Even-length palindrome.

                # Update longest if a longer palindrome is found.
                longest = max(longest, odd_pal, even_pal, key=len)

            return longest

    ---

    ## 4. Detailed Step-by-Step Explanation

    ### 4.1. The expandAroundCenter Function

    This function is the heart of the algorithm. It takes two indices—`left` and `right`—and expands outward to find the longest palindrome with that center.

    #### How It Works:

    1. **Initial Check:**  
       The function starts with the pointers `left` and `right`. These pointers can be the same (for odd-length palindromes) or adjacent (for even-length palindromes).

    2. **The While Loop:**  
       while left >= 0 and right < len(s) and s[left] == s[right]:
           left -= 1
           right += 1

       - **Conditions:**
         - left >= 0: Ensures we do not go before the start of the string.
         - right < len(s): Ensures we do not go past the end of the string.
         - s[left] == s[right]: Checks that the characters are the same (palindrome property).
       - **Action:**
         If all conditions are met, the function moves left one position to the left and right one position to the right—thus "expanding" the window.

    3. **Returning the Palindrome:**  
       When the while loop stops (either a mismatch is found or boundaries are exceeded), the current left and right are one position outside the valid palindrome. The function then returns:
       return s[left + 1:right]
       This returns the substring that is a palindrome.

    ---

    ### 4.2. Visualizing the Expansion

    #### Example 1: Odd-Length Palindrome ("babad")

    **String:** "babad"

    **Using Center at Index 2 ('b'):**

    1. **Initial State:**
       - Indices: 0  1  2  3  4
       - Characters: b  a  b  a  d
       - Start: left = 2, right = 2
       - Diagram:
             0   1   2   3   4
             b   a   b   a   d
                     ↑
                  (center)

    2. **First Expansion:**
       - Compare s[2] with s[2] → 'b' == 'b' (True).
       - Expand: left becomes 1, right becomes 3.
       - Diagram:
             0   1   2   3   4
             b   a   b   a   d
                 ↑       ↑
             left=1   right=3

    3. **Second Expansion:**
       - Compare s[1] with s[3] → 'a' == 'a' (True).
       - Expand: left becomes 0, right becomes 4.
       - Diagram:
             0   1   2   3   4
             b   a   b   a   d
             ↑               ↑
           left=0         right=4

    4. **Third Expansion:**
       - Compare s[0] with s[4] → 'b' != 'd' (False).
       - Stop expanding.

    5. **Return:**  
       The valid palindrome is from index left+1 = 1 to right-1 = 3:
       s[1:4] = "aba"

    #### Example 2: Even-Length Palindrome ("abba")

    **String:** "abba"

    **Using Center Between Indices 1 and 2:**

    1. **Initial State:**
       - Indices: 0  1  2  3
       - Characters: a  b  b  a
       - Start: left = 1, right = 2
       - Diagram:
             0   1   2   3
             a   b   b   a
                 ↑   ↑
             left=1, right=2

    2. **First Expansion:**
       - Compare s[1] with s[2] → 'b' == 'b' (True).
       - Expand: left becomes 0, right becomes 3.
       - Diagram:
             0   1   2   3
             a   b   b   a
             ↑           ↑
           left=0     right=3

    3. **Second Expansion:**
       - Compare s[0] with s[3] → 'a' == 'a' (True).
       - Expand: left becomes -1, right becomes 4 (pointers go out of bounds).
       - Diagram:
             0   1   2   3
             a   b   b   a
          left becomes -1 and right becomes 4 → Stop

    4. **Return:**  
       The valid palindrome is from index left+1 = 0 to right-1 = 3:
       s[0:4] = "abba"

    ---

    ## 5. Final Takeaways

    - **Center Detection:**  
      The code “jumps” directly to the center using:
          odd_pal = expandAroundCenter(i, i)
          even_pal = expandAroundCenter(i, i + 1)
      These calls set the starting positions for expansion.

    - **Expansion:**  
      The expandAroundCenter function expands outwards as long as the characters on the left and right are equal. This process exploits the symmetry of palindromes.

    - **Efficiency:**  
      The overall algorithm has a time complexity of O(n²), which is efficient enough for the problem constraints and excellent for an interview discussion.

    - **Visualization:**  
      The ASCII diagrams help to see how the pointers move during the expansion process for both odd-length and even-length palindromes.

    ---

    ## 6. Summary

    This document covers:
    - The problem statement and expected outputs.
    - The core idea behind the Expand-Around-Center algorithm.
    - Detailed code with step-by-step explanations.
    - Visual diagrams to help understand how the expansion works.
    - Final takeaways that summarize how and why the approach works.

    Use this document to study and understand the algorithm so that you can explain it confidently in your interviews. Now, go rock that interview and show them you’re a master of palindromic substrings!

    *End of Document*
    """
