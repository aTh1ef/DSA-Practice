class Solution:
    def beautySum(self, s: str) -> int:
        total = 0  # This variable will store the total sum of beauties for all substrings.
        n = len(s)  # Length of the input string.

        # Outer loop: choose every possible starting index for a substring.
        for i in range(n):
            freq = [0] * 26  # Frequency array for letters 'a' to 'z' (initialized to 0).

            # Inner loop: extend the substring from index i to j.
            for j in range(i, n):
                # Update frequency for character s[j].
                # ord(s[j]) gives the ASCII code of s[j]. Subtracting ord('a') converts it to an index (0 to 25).
                freq[ord(s[j]) - ord('a')] += 1

                # Compute the beauty of the current substring s[i:j+1].
                # Beauty = (maximum frequency among characters) - (minimum frequency among characters)
                max_freq = 0  # Initialize maximum frequency.
                min_freq = float('inf')  # Initialize minimum frequency as infinity.

                # Check each frequency in our frequency array.
                for count in freq:
                    if count > 0:  # Only consider characters that actually appear in the substring.
                        max_freq = max(max_freq, count)  # Update maximum frequency.
                        min_freq = min(min_freq, count)  # Update minimum frequency.

                # Calculate beauty for this substring.
                beauty = max_freq - min_freq

                # Add the beauty value to the total sum.
                total += beauty

        return total  # Return the total sum of beauties for all substrings.

if __name__ == "__main__":
    s = "aabc"
    sol = Solution()
    answer = sol.beautySum(s)
    print(answer)

    """
    ===============================================================================
    LeetCode 1781: Sum of Beauty of All Substrings
    ===============================================================================

    PROBLEM STATEMENT:
    ------------------
    The beauty of a substring is defined as the difference between the frequency 
    of its most frequent character and the frequency of its least frequent character 
    (only considering characters that actually appear in the substring).

    For a given string s, calculate the sum of the beauty of all its substrings.

    For example:
      s = "aabcb"

      Consider the substring "aab":
        - Characters: a, a, b
        - Frequency: a = 2, b = 1
        - Beauty = max(2, 1) - min(2, 1) = 2 - 1 = 1

    If you sum up the beauty for all substrings of "aabcb", you get 5.

    ===============================================================================
    APPROACH:
    ----------
    1. Use two nested loops to generate all possible substrings.
    2. For each substring, maintain a frequency array (size 26 for 'a'-'z') to count
       the occurrences of each character.
    3. Compute the maximum frequency (maxFreq) and the minimum frequency (minFreq)
       among characters that appear in the substring.
    4. The beauty of that substring is maxFreq - minFreq.
    5. Sum the beauty values for all substrings and return the total.

    Time Complexity: O(N^2)
    - There are O(N^2) substrings.
    - Updating the frequency array and computing max/min over 26 elements is O(1).

    ===============================================================================
    VISUALIZATION & ASCII DIAGRAM (Example: "aabcb")
    ===============================================================================
    Let's consider s = "aabcb" and focus on the substring "aab" (i = 0, j = 2):

    Indices:     0    1    2    3    4
    Characters:  a    a    b    c    b

    For substring "aab" (from index 0 to 2):
      - Characters: a, a, b
      - Frequency:
           a: 2
           b: 1
           (others: 0, ignored)
      - Calculation:
           maxFreq = 2 (for 'a')
           minFreq = 1 (for 'b')
           Beauty = 2 - 1 = 1

    This value (1) is added to the total beauty sum.

    ===============================================================================
    KEY LINE EXPLANATION:
    ===============================================================================
    freq[ord(s[j]) - ord('a')] += 1

    - s[j]:
        The current character in the string at index j.

    - ord(s[j]):
        Returns the ASCII (or Unicode) code of s[j]. 
        For example, ord('a') returns 97, ord('b') returns 98, etc.

    - ord('a'):
        Returns 97, which is the ASCII code for 'a'.

    - ord(s[j]) - ord('a'):
        Normalizes the ASCII code so that:
          - 'a' maps to 0  (97 - 97 = 0)
          - 'b' maps to 1  (98 - 97 = 1)
          - 'c' maps to 2  (99 - 97 = 2)
        This gives an index in the range 0 to 25 for letters 'a' to 'z'.

    - freq[...]:
        Accesses the frequency array at the index corresponding to s[j].

    - += 1:
        Increments the count of the character s[j] in the frequency array.

    ===============================================================================
    DETAILED CODE WITH EXPLANATIONS:
    ===============================================================================
    """

    """
    ===============================================================================
    STEP-BY-STEP EXAMPLE WITH "aabcb":
    ===============================================================================
    Let s = "aabcb", n = 5

    --- Iteration when i = 0 (Substrings starting at index 0) ---
    Substring when j = 0: "a"
       - freq becomes: [1, 0, 0, ...] (only 'a' has appeared once)
       - maxFreq = 1, minFreq = 1  → Beauty = 1 - 1 = 0
       - Total so far: 0

    Substring when j = 1: "aa"
       - freq becomes: [2, 0, 0, ...] ('a' appears twice)
       - maxFreq = 2, minFreq = 2  → Beauty = 2 - 2 = 0
       - Total so far: 0

    Substring when j = 2: "aab"
       - freq becomes: [2, 1, 0, ...] ('a' appears 2 times, 'b' appears once)
       - maxFreq = 2, minFreq = 1  → Beauty = 2 - 1 = 1
       - Total so far: 0 + 1 = 1

    Substring when j = 3: "aabc"
       - freq becomes: [2, 1, 1, 0, ...] ('a':2, 'b':1, 'c':1)
       - maxFreq = 2, minFreq = 1  → Beauty = 2 - 1 = 1
       - Total so far: 1 + 1 = 2

    Substring when j = 4: "aabcb"
       - freq becomes: [2, 2, 1, 0, ...] ('a':2, 'b':2, 'c':1)
       - maxFreq = 2, minFreq = 1  → Beauty = 2 - 1 = 1
       - Total so far: 2 + 1 = 3

    --- Iteration when i = 1 (Substrings starting at index 1, s[1:] = "abcb") ---
    Substring "a" (s[1:2]): "a"
       - freq resets: [0,...] then becomes: [1, 0, 0, ...]
       - Beauty = 0
    Substring "ab" (s[1:3]): "ab"
       - freq: [1, 1, 0, ...]
       - Beauty = 1 - 1 = 0
    Substring "abc" (s[1:4]): "abc"
       - freq: [1, 1, 1, ...]
       - Beauty = 1 - 1 = 0
    Substring "abcb" (s[1:5]): "abcb"
       - freq: [1, 2, 1, ...]
       - Beauty = 2 - 1 = 1
       - Total so far: 3 + 1 = 4

    --- Iteration when i = 2 (Substrings starting at index 2, s[2:] = "bcb") ---
    Substring "b" (s[2:3]): "b"
       - freq: [0, 1, 0, ...]
       - Beauty = 0
    Substring "bc" (s[2:4]): "bc"
       - freq: [0, 1, 1, ...]
       - Beauty = 1 - 1 = 0
    Substring "bcb" (s[2:5]): "bcb"
       - freq: [0, 2, 1, ...]
       - Beauty = 2 - 1 = 1
       - Total so far: 4 + 1 = 5

    --- Iterations for i = 3 and i = 4 ---
    These yield substrings with beauty = 0.

    ===============================================================================
    FINAL RESULT:
    ===============================================================================
    For s = "aabcb", the function beautySum returns 5.

    ===============================================================================
    Takeaway:
    ----------
    This code iterates through every substring, updates the frequency of characters using 
    a fixed array, and computes the beauty (max frequency minus min frequency) for each substring.
    The sum of all these beauty values is returned as the final result.
    ===============================================================================
    """