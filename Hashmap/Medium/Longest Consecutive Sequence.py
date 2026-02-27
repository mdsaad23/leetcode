"""
PROBLEM STATEMENT:
Given an unsorted array of integers 'nums', return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

# ==========================================
# USER SOLUTION 1 ANALYSIS
# ==========================================
# Solution Approach:
# • Sorting and Hash Map: The user sorts the array first to bring consecutive numbers together.
# • Linear Scan with State: Uses a dictionary 'h' to store the length of the consecutive sequence ending at each number.
# • Handling Duplicates: Explicitly checks if a number is already in the hash map to skip redundant processing.
# • Counter Logic: Increments a counter if the previous consecutive number (nums[i]-1) exists in the map; otherwise, resets to 1.

# Time Complexity: O(N log N) - Dominating factor is the sorting step (nums = sorted(nums)).
# Space Complexity: O(N) - Storing elements and their sequence counts in the dictionary 'h'.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            h={}
            counter=0
            nums=sorted(nums)
            for i in range(len(nums)):
                if nums[i] in h:
                    continue
                elif nums[i]-1 in h:
                    counter+=1
                    h[nums[i]]=counter
                else:
                    counter=1
                    h[nums[i]]=counter
            return max(h.values())
        else:
            return 0

# ==========================================
# USER SOLUTION 2 ANALYSIS (OPTIMAL)
# ==========================================
# Solution Approach:
# • Hash Set for O(1) Lookups: Converts the list to a set to eliminate duplicates and allow constant time element checking.
# • Sequence Start Identification: The core logic identifies the "start" of a sequence by checking if (n - 1) is NOT in the set.
# • While Loop Expansion: Once a start is found, it counts how many subsequent numbers (n + 1, n + 2...) exist in the set.
# • Efficiency: Even with a nested while loop, each number is visited at most twice (once by the for loop and once by the while loop), ensuring linear time.

# Time Complexity: O(N) - Linear scan of the set and total expansion iterations are bounded by N.
# Space Complexity: O(N) - Storing the unique elements in a Hash Set.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        longest=0
        for n in nums:
            if n-1 not in nums:
                curr=1
                while n+curr in nums:
                    curr+=1
                longest=max(longest,curr)

        return longest

# ==========================================
# OPTIMAL APPROACH SUMMARY
# ==========================================
# • Requirement: The problem explicitly asks for O(n) time complexity.
# • Strategy: Use a Hash Set (Solution 2). 
# • Why Solution 2 is better than Solution 1: 
#   1. Solution 1 uses Sorting, which makes it O(N log N).
#   2. Solution 2 utilizes the mathematical property that a sequence start has no 'n-1' predecessor.
#   3. Solution 2 avoids the extra overhead of `max(h.values())` which requires another O(N) pass.

# ==========================================
# REAL-WORLD APPLICATION
# ==========================================
# 1. Database Indexing:
#    In relational databases, identifying consecutive ranges of primary keys or timestamps is crucial for 
#    optimizing range queries and detecting gaps in sequential data (e.g., finding missing invoice numbers).
#
# 2. Network Packet Reassembly:
#    When data packets arrive out of order via TCP, the system must identify the longest sequence of 
#    consecutive packets it can "release" to the application layer while waiting for missing sequence numbers.
#
# 3. Bioinformatics (Genomics):
#    Researchers look for the longest consecutive segments of specific DNA markers or base pairs 
#    to identify gene structures or regions of interest within a large, unsorted dataset of genetic fragments.
#
# 4. Warehouse & Logistics:
#    Optimizing picking routes by identifying consecutive bin locations or tracking contiguous time slots 
#    for scheduling deliveries to maximize resource utilization.