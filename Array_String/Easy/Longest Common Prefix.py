"""
PROBLEM STATEMENT:
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

SOLUTION APPROACH (Horizontal Scanning):
* The user implemented a "Horizontal Scanning" approach.
* It initializes the potential prefix (lcp) as the first string in the list.
* The algorithm iterates through the remaining strings one by one.
* For each new string, it compares characters with the current prefix to find the length of the matching part.
* It updates the prefix length (c) to the length of the common match found so far.
* This process continues until all strings are processed or the common prefix becomes empty.

COMPLEXITY ANALYSIS:
* Current Time Complexity: O(S), where S is the sum of all characters in all strings. In the worst case, we compare every character.
* Current Space Complexity: O(1), as we only store the index/length 'c' and the result slice.
* Optimal Time Complexity: O(S) - The horizontal/vertical scanning approaches are both optimal in terms of time.
* Optimal Space Complexity: O(1) or O(m) depending on whether the output string is counted.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        elif strs[0]=="":
            return ""
        lcp = strs[0]
        c=len(lcp)
        for i in range(1,len(strs)):
            j=0
            while j<c and j<len(strs[i]):
                if strs[i][j]==lcp[j]:
                    j+=1
                else:
                    c=j
            c=j
                    
        if c==0:
            return ""
        else:
            return lcp[:c]

"""
REAL-WORLD APPLICATION:
The logic of finding common prefixes is fundamental in various computer science systems:

1. Autocomplete and Search Suggestions: 
   Search engines and IDEs use prefix matching to suggest completions. When you type "pyth", 
   the system identifies the common prefix across its database to suggest "python" or "python3".

2. IP Routing (Longest Prefix Match):
   In networking, routers use Longest Prefix Matching (LPM) in IP forwarding tables to decide 
   the next hop for a packet. The router looks for the longest prefix in the routing table 
   that matches the destination IP address.

3. File Systems and URI Routing:
   Web frameworks (like Django or Flask) use prefix matching to route incoming URLs to the 
   correct controller. Similarly, version control systems like Git use common prefixes to 
   organize and compress object hashes.
"""
