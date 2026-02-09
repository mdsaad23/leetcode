"""
PROBLEM STATEMENT:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""

"""
SOLUTION APPROACH: Frequency Counter (Single Hash Map)
* Length Validation: The algorithm first checks if the two strings have the same length. 
  If not, they cannot be anagrams.
* Hash Map Counting: A single dictionary (hash map) is used to track character frequencies.
* Increment/Decrement Logic: The code iterates through both strings simultaneously using 
  the same index. For string 's', it increments the count of the character; for string 't', 
  it decrements the count.
* Balanced Check: Finally, it iterates through the hash map values. If all counts are zero, 
  it confirms both strings have the exact same character distribution.

Complexity Analysis:
- Time Complexity: O(n)
  The algorithm iterates through the strings once and then through the unique characters 
  in the hash map.
- Space Complexity: O(k)
  Where k is the number of unique characters (O(1) if limited to 26 lowercase English letters).

Optimal Complexity:
- Time: O(n)
- Space: O(1) (for a fixed alphabet size like 26 letters)
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s=len(s)
        k={}
        if len_s != len(t):
            return False
        
        for i in range(len_s):
            if s[i] not in k:
                k[s[i]]=1
            else:
                k[s[i]]+=1
            if t[i] not in k:
                k[t[i]]=-1
            else:
                k[t[i]]-=1
        for i in k:
            if k[i]!=0:
                return False
        return True

"""
REAL-WORLD APPLICATION:
The logic of frequency counting and character distribution is a fundamental 
concept in computer science used across various high-scale systems:

1. Search Engines & Natural Language Processing (NLP):
   Used in 'Bag of Words' models to compare document similarity or to detect 
   paraphrasing and near-duplicate content.

2. Database Indexing & Data Integrity:
   Checksums and hashing algorithms often use similar frequency-based logic 
    to ensure that data packets sent over a network have not been altered.

3. Cryptography & Security:
   Frequency analysis is a core technique in breaking classical substitution 
   ciphers by comparing the frequency of characters in encrypted text to 
   standard language distributions.

4. E-commerce & Inventory Management:
   The "increment for entry, decrement for exit" logic is used to maintain 
   real-time stock levels in high-concurrency systems.
"""
