# PROBLEM STATEMENT
# Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to 'target'.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1] (Because nums[0] + nums[1] == 9)

# SOLUTION APPROACH: ONE-PASS HASH MAP (DICTIONARY)
# • The user utilizes a Python dictionary 'h' to store the value of each element as a key and its index as the value.
# • For every element, the code calculates the 'complement' (target - current_value).
# • It checks if this complement already exists in the dictionary. 
# • If it exists, the pair is found and the indices are returned.
# • If not, the current element is added to the dictionary to be potentially used as a complement for future elements.
#
# COMPLEXITY ANALYSIS:
# • Current Time Complexity: O(n) - The array is traversed only once.
# • Current Space Complexity: O(n) - In the worst case, the dictionary stores almost all elements of the array.
# • Optimal Complexity: O(n) Time | O(n) Space. The user's solution is already optimal for an unsorted array.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            if (target-nums[i]) in h:
                return [i,h[target-nums[i]]]
            h[nums[i]]=i

# REAL-WORLD APPLICATION
# The logic of using Hash Maps for rapid lookups is a cornerstone of modern software engineering:
#
# • Database Indexing: Databases use hash-based indexing to find records in O(1) time rather than scanning millions of rows (O(n)).
# • Caching & Memoization: Web servers store frequently accessed data in a "Key-Value" cache (like Redis) to avoid expensive re-computations.
# • Fraud Detection: Payment systems use similar "complement" logic to flag duplicate transactions occurring within a specific time window.
# • E-commerce Search: Quickly matching user filters (tags) to product IDs in large catalogs.