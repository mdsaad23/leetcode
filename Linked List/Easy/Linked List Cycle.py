"""
PROBLEM STATEMENT: LINKED LIST CYCLE
-----------------------------------------
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, 'pos' is used to denote 
the index of the node that tail's next pointer is connected to. 

Note that 'pos' is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

# USER'S SOLUTION APPROACH:
# 1. Pattern: Floyd's Tortoise and Hare (Two Pointers).
# 2. Logic: Initialize two pointers, 'slow' and 'fast', at the head of the list.
# 3. Iteration: 'slow' moves one step at a time, while 'fast' moves two steps.
# 4. Detection: If there is a cycle, the 'fast' pointer will eventually wrap around 
#    and meet the 'slow' pointer. If 'fast' reaches the end (None), no cycle exists.
#
# USER'S COMPLEXITY ANALYSIS:
# - Time Complexity: O(N), where N is the number of nodes in the linked list.
# - Space Complexity: O(1), as no extra data structures are used.

# --- USER'S ORIGINAL CODE ---
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

# OPTIMAL SOLUTION APPROACH:
# - The user's implementation is already the optimal approach for this problem.
# - Alternative Approach: A Hash Set could store visited nodes, but it would 
#   increase Space Complexity to O(N).
# - Optimal Complexity:
#   - Time: O(N)
#   - Space: O(1)

# --- OPTIMAL CODE ---
class OptimalSolution(object):
    def hasCycle(self, head):
        # Initial check for empty list or single node without cycle
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            if slow == fast:          # Cycle detected
                return True
                
        return False

"""
REAL-WORLD APPLICATION:
-----------------------------------------
The logic of cycle detection is fundamental in computer science and distributed systems:

1. Distributed Systems (Deadlock Detection): In operating systems or databases, 
   resource allocation graphs are analyzed for cycles. A cycle represents a 
   'Deadlock' where processes are waiting on each other indefinitely.

2. Network Routing: Routing protocols (like BGP or OSPF) must ensure that 
   data packets do not enter an infinite loop while traveling between routers, 
   which would consume bandwidth and crash the network.

3. Garbage Collection: Programming languages like Python use reference counting 
   and cycle-detection algorithms to identify groups of objects that reference 
   each other but are no longer reachable from the main program, allowing the 
   system to reclaim memory.

4. Financial Systems: Detecting "Circular Trading" or "Round-Tripping" in 
   stock markets or banking, where a series of transactions eventually 
   returns to the original party to artificially inflate volume or hide debt.
"""