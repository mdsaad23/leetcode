"""
PROBLEM STATEMENT
-----------------
Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.


SOLUTION APPROACH (User's Implementation)
-----------------------------------------
* Stack-Based Processing: The user utilizes a list as a stack to maintain the 
  order of opening brackets encountered.
* Linear Traversal: The code iterates through the string character by character 
  using a for-loop.
* Conditional Logic: 
    - If an opening bracket ('(', '[', '{') is found, it is pushed onto the stack.
    - If a closing bracket is found, the code checks if the stack is empty (invalid) 
      or if the top of the stack matches the current closing bracket.
* Final Validation: After the loop, the code returns True only if the stack is 
  empty, ensuring all brackets were properly closed.

COMPLEXITY ANALYSIS
-------------------
* Current Time Complexity: O(n) - The string is traversed exactly once.
* Current Space Complexity: O(n) - In the worst case (e.g., "((((("), the stack 
  stores all characters.
* Optimal Time Complexity: O(n)
* Optimal Space Complexity: O(n)
Note: Your current solution is already optimal in terms of Big-O complexity.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        for i in range(len(s)):
            if s[i] in {"(","[","{"}:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if (s[i]==")" and stack[-1]=="(") or (s[i]=="]" and stack[-1]=="[") or (s[i]=="}" and stack[-1]=="{"):
                    stack.pop()
                else:
                    return False
        return not stack

"""
OPTIMAL SOLUTION (Refactored for Readability)
--------------------------------------------
While your solution is optimal in complexity, using a dictionary (hash map) 
to store bracket pairs makes the code cleaner and easier to maintain.
"""

def isValid_Optimal(s):
    stack = []
    # Mapping closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # Pop the top element if stack is not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the mapping matches the popped element
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push to stack
            stack.append(char)
            
    return not stack

"""
REAL-WORLD APPLICATION
----------------------
The logic of matching pairs and maintaining order via stacks is fundamental 
in software engineering:

* Compiler Design: Compilers use this logic during the 'syntax analysis' phase 
  to ensure that code blocks (curly braces) and function calls are properly nested.
* Data Serialization: Parsing formats like JSON or XML requires ensuring every 
  opening tag/brace has a matching closing tag/brace in the correct LIFO order.
* Undo/Redo Mechanisms: Many text editors use stack structures to manage the 
  history of actions, ensuring the last action taken is the first one reversed.
* Integrated Development Environments (IDEs): Features like 'Bracket Highlighting' 
  in VS Code or PyCharm use this algorithm in real-time to help developers 
  identify missing or mismatched enclosures.
"""