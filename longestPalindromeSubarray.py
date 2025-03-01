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