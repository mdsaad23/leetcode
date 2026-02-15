"""
PROBLEM STATEMENT:
------------------
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a 
   cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false

SOLUTION APPROACH (USER IMPLEMENTATION):
----------------------------------------
* Type: Hashing / Cycle Detection using a Set (Dictionary)
* The solution converts the integer to a string to iterate through digits easily.
* It calculates the sum of squares of the digits in a loop.
* A dictionary (`h_sumprod`) is used to store previously encountered sums to detect cycles.
* If the sum becomes 1, the function returns True.
* If the sum is found in the dictionary, it indicates an infinite loop that doesn't reach 1, 
    so the function returns False.

COMPLEXITY ANALYSIS:
--------------------
* User Time Complexity: O(log n * log(log n)) - Determining the next value involves string conversion 
    and digit iteration, and the number of steps to reach 1 or a cycle is relatively small.
* User Space Complexity: O(log n) - To store seen numbers in the dictionary and the string representation.
* Optimal Time Complexity: O(log n) - Using Floyd's Cycle-Finding Algorithm (Slow/Fast pointers) 
    can reduce overhead.
* Optimal Space Complexity: O(1) - Cycle detection via pointers avoids extra storage for a hash set.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        sumprod=n
        n_str = str(n)
        h_sumprod={}
        while sumprod>1:
            sumprod=0
            for i in range(len(n_str)):
                sumprod+=(int(n_str[i]))**2
            if sumprod==1:
                return True
            elif sumprod in h_sumprod:
                return False
            else:
                h_sumprod[sumprod]=sumprod
                n_str=str(sumprod)
        return True

"""
REAL-WORLD APPLICATION:
-----------------------
The underlying logic of this problem—Cycle Detection—is critical in various computer science domains:

1.  Distributed Systems: Identifying "deadlocks" or infinite loops in resource allocation 
    graphs where processes are waiting on each other indefinitely.
2.  Network Routing: Detecting loops in packet forwarding paths (e.g., TTL in IP headers 
    or Spanning Tree Protocol) to prevent network congestion.
3.  Cryptography: Random number generators and stream ciphers rely on cycle detection 
    to ensure that the generated sequences do not repeat too quickly, which would 
    make the encryption vulnerable.
4.  Data Integrity: Used in pointer-based data structures (like linked lists) to ensure 
    there is no corruption that leads to an infinite traversal.
"""




###################     OPTIMAL SOLUTION (FLOYD'S CYCLE-FINDING ALGORITHM)     ###################
"""
OPTIMAL PROBLEM STATEMENT:
--------------------------
Determine if a number n is "happy" using an approach with constant space complexity.

OPTIMAL SOLUTION APPROACH:
--------------------------
* Type: Floyd's Cycle-Finding Algorithm (Two Pointers)
* Step 1: Define a helper function `getNext(n)` to calculate the sum of the squares of digits.
* Step 2: Initialize two pointers, `slow` starting at `n` and `fast` starting at `getNext(n)`.
* Step 3: Move `slow` by one step and `fast` by two steps in a loop.
* Step 4: If `fast` reaches 1, the number is happy (return True).
* Step 5: If `slow` and `fast` meet at any other number, a cycle is detected (return False).

COMPLEXITY ANALYSIS:
--------------------
* Optimal Time Complexity: O(log n) - The number of steps to enter a cycle or reach 1 is logarithmic 
    relative to the value of n.
* Optimal Space Complexity: O(1) - No extra data structures (sets/dicts) are used; only 
    two integer variables for pointers.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                # Use modulo and floor division to avoid string conversion
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        
        # Move until they meet or fast hits 1
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))

        return fast_runner == 1

"""
REAL-WORLD APPLICATION:
-----------------------
This specific 'Two-Pointer' optimization is a staple in high-performance computing:

1.  Memory Management: Detecting circular references in garbage collection 
    algorithms to prevent memory leaks.
2.  Database Systems: Detecting cycles in transaction dependency graphs to 
    prevent and resolve deadlocks in concurrent environments.
3.  Telecommunications: Managing buffer queues where pointers must wrap around 
    without causing infinite loops or data overwrites.
"""