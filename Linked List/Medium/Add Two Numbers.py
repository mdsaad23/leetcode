"""
PROBLEM STATEMENT:
------------------
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

# SOLUTION APPROACH (USER):
# -------------------------
# * Iterative Linked List Traversal: The solution uses a single while loop to traverse both linked lists simultaneously.
# * Dummy Head Technique: Initializes a 'start' (dummy) node to simplify the management of the head of the resulting list.
# * Manual Carry Handling: Calculates the sum of values and the carry at each step using modulo (%) and integer division (//).
# * Null Safety: Includes checks (if l1 / if l2) to handle cases where the linked lists are of unequal lengths.
# * Termination Condition: The loop continues as long as there is a node in l1, a node in l2, or a remaining carry to process.

# USER'S ORIGINAL CODE:
# ---------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry=0
        start = ListNode(0)
        fin = start

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            fin.next = ListNode((a+b+carry)%10)
            fin = fin.next
            carry = (a+b+carry)//10
            if l1 : l1=l1.next
            if l2 : l2=l2.next
        return start.next

# COMPLEXITY ANALYSIS (USER CODE):
# --------------------------------
# Time Complexity: O(max(N, M)), where N and M are the lengths of l1 and l2 respectively. The loop runs for the duration of the longest list.
# Space Complexity: O(max(N, M)), as we create a new linked list to store the sum.

# OPTIMAL APPROACH:
# -----------------
# * The user's solution is already optimal in terms of Big O complexity.
# * Efficiency Note: Instead of re-calculating (a+b+carry) twice, storing the intermediate sum in a variable slightly improves performance.
# * Cleanliness: Using a dummy node is the industry standard for linked list construction to avoid edge-case logic for the head node.

# OPTIMAL CODE:
# -------------
class OptimalSolution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry efficiently
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            curr.next = ListNode(total_sum % 10)
            
            # Move pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next

# OPTIMAL COMPLEXITY:
# -------------------
# Time Complexity: O(max(N, M)) - Each node is visited exactly once.
# Space Complexity: O(max(N, M)) - Required to store the result.

"""
REAL-WORLD APPLICATION:
-----------------------
1. Arbitrary-Precision Arithmetic (BigInt):
   Standard data types (like 64-bit integers) have limits. When calculating numbers with hundreds or thousands 
   of digits (used in Cryptography or Scientific Computing), computers represent numbers as linked lists or 
   arrays of digits. This logic is the foundation for performing addition on those 'BigInt' structures.

2. Financial Systems:
   In banking systems where precision is critical and numbers can exceed standard memory limits, 
   the manual carry/sum logic ensures no precision is lost due to floating-point errors.

3. Signal Processing:
   Representing sequential data streams where elements must be processed one by one (similar to linked 
   list nodes) while maintaining a 'state' (like a carry) between cycles.
"""