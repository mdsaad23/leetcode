"""
PROBLEM DESCRIPTION:
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
"""

class Solution(object):
    
    # -----------------------------------------------------------
    # SOLUTION 1: Pythonic Approach (Built-in)
    # -----------------------------------------------------------
    """
    SOLUTION APPROACH 1:
    Using Built-in String Methods - O(N) Time, O(N) Space
    
    1. s.split(): Splits the string into a list of words. 
       - Crucially, Python's default split() without arguments automatically handles 
         multiple spaces and removes leading/trailing whitespace.
       - Example: "   fly me   to   the moon  " -> ['fly', 'me', 'to', 'the', 'moon']
    2. Access [-1]: We grab the last element of the list.
    3. Return len(): Return the length of that string.
    """
    def lengthOfLastWord_BuiltIn(self, s):
        return len(s.split()[-1])

    # -----------------------------------------------------------
    # SOLUTION 2: Pointer Iteration (Algorithmic)
    # -----------------------------------------------------------
    """
    SOLUTION APPROACH 2:
    Reverse Iteration - O(N) Time, O(1) Space
    
    1. Initialize 'e_pointer' at the very end of the string.
    2. Trim Trailing Spaces: Move 'e_pointer' backwards until we hit a non-space character.
       This marks the end of the last word.
    3. Find Start of Word: Initialize 's_pointer' just before 'e_pointer'.
       Move 's_pointer' backwards until we hit a space OR the beginning of the string.
    4. Calculate Length: The distance between the end pointer and the start pointer 
       (e_pointer - s_pointer) gives the length of the word.
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        e_pointer=len(s)-1
        
        # Step 1: Skip trailing spaces to find the last character of the last word
        while s[e_pointer]==' ':
            e_pointer-=1
            
        # Step 2: Traverse backwards to find the start of the word
        s_pointer=e_pointer-1
        while s_pointer>=0 and s[s_pointer]!=' ':
            s_pointer-=1
            
        return e_pointer-s_pointer