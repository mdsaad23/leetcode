"""
PROBLEM DESCRIPTION:
28. Find the Index of the First Occurrence in a String

Given two strings 'haystack' and 'needle', return the index of the first occurrence of 
'needle' in 'haystack', or -1 if 'needle' is not part of 'haystack'.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

"""
SOLUTION APPROACH:
Sliding Window (Slicing) - O((N-M)*M) Time

1. We define a window of size 'len_n' (length of the needle).
2. We iterate through the 'haystack' one character at a time.
   - The loop range is restricted to `len(haystack) - len_n + 1`. This prevents 
     IndexErrors by stopping when there aren't enough characters left in haystack 
     to form the needle.
3. In each iteration, we extract a substring from the haystack: `haystack[i : i+len_n]`.
4. Comparison: We compare this extracted substring directly with the 'needle'.
5. If they match, we immediately return the current index 'i'.
6. If the loop completes without a match, return -1.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_n = len(needle)
        # Iterate only as far as necessary (Haystack length - Needle length)
        for i in range(len(haystack)-len_n+1):
            # Check the "window" of text starting at i
            if haystack[i:i+len_n]==needle[:]:
                return i
        return -1