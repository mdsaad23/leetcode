"""
PROBLEM STATEMENT: CONTAINS DUPLICATE II
Link: https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array 'nums' and an integer 'k', return true if there are two 
distinct indices 'i' and 'j' in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

# SOLUTION APPROACH USED BY USER:
# - Hash Map (Dictionary) Tracking: The user utilizes a hash map to store the most recent index of each value encountered.
# - Single Pass: The algorithm iterates through the list once.
# - Index Comparison: If a value is seen again, the current index is compared with the stored index to check the distance constraint (<= k).
# - Update Logic: If the distance is greater than k, the stored index is updated to the current index, as this is now the closest potential candidate for future duplicates.

# USER'S ORIGINAL CODE:
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h={}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]]=i
            else:
                if i-h[nums[i]]<=k:
                    return True
                else:
                    h[nums[i]]=i
        return False

# COMPLEXITY ANALYSIS (USER CODE):
# - Time Complexity: O(n), where n is the number of elements in nums. Each lookup and insertion in the hash map takes O(1) on average.
# - Space Complexity: O(n) in the worst case, as the hash map might store every element in the array if no duplicates satisfy the condition.

# OPTIMAL APPROACH: SLIDING WINDOW (SET)
# - While the Hash Map approach is O(n), a "Sliding Window" using a Hash Set is often considered more space-efficient in practice for large k.
# - Maintain a set of size k.
# - If the current element is in the set, a duplicate within distance k exists.
# - If the set size exceeds k, remove the oldest element (nums[i-k]).
# - Optimal Time Complexity: O(n)
# - Optimal Space Complexity: O(min(n, k))

class OptimalSolution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            # If element is already in the window of size k, we found a duplicate
            if num in window:
                return True
            
            window.add(num)
            
            # Keep the window size at k by removing the oldest element
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False

"""
REAL-WORLD APPLICATION:

1. Data Deduplication in Streaming:
   In high-frequency data streams (like stock market tickers or IoT sensor data), 
   systems often need to filter out 'noisy' duplicate signals that occur within 
   a specific time window or sequence length. This logic prevents redundant 
   processing of the same data point.

2. Fraud Detection (Velocity Checks):
   Payment processors use similar windowing logic to detect "carding" or rapid-fire 
   transactions. If the same credit card number appears twice within a very 
   short index of transactions (time/sequence), it triggers a fraud alert.

3. Cache Replacement Policies:
   The concept of tracking the 'last seen' index of a piece of data is fundamental 
   to Least Recently Used (LRU) caching mechanisms, ensuring that frequently 
   accessed data stays available while stale data is evicted.

4. Web Browser History & Session Management:
   Detecting if a user has revisited the same URL within a certain number of clicks 
   to optimize "Back" button behavior or to prevent circular navigation loops.
"""