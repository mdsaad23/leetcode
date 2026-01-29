"""
PROBLEM DESCRIPTION:
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
"""

"""
SOLUTION APPROACH:
Sorting + Two Pointers Strategy - O(N^2) Time

1. Sort the Array: This is critical. Sorting allows us to efficiently skip duplicates 
   and use the two-pointer technique.

2. Iterate with 'i': We iterate through the array, fixing one number 'nums[i]'.
   - Skip Duplicates: If nums[i] == nums[i-1], continue to avoid duplicate triplets.
   - Optimization: If nums[i] > 0, break immediately (impossible to sum to 0 if the smallest number is positive).

3. Two Pointers ('l' and 'r'): Treat the remaining part as a "Two Sum" problem on the subarray nums[i+1:].
   - 'l' starts at i+1, 'r' starts at len(nums)-1.

4. Convergence:
   - If sum == 0: Found a triplet! Add to result. Crucially, increment 'l' and decrement 'r' 
     past any duplicate values to prevent recording the same triplet twice.
   - If sum > 0: Too large, decrement 'r'.
   - If sum < 0: Too small, increment 'l'.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            # Skip duplicates for the first element
            if i>0 and nums[i]==nums[i-1]:
                continue
            # Optimization: If smallest number is > 0, sum cannot be 0
            if nums[i]>0:
                break
            
            l=i+1
            r=len(nums)-1
            
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    result.append([nums[i],nums[l],nums[r]])
                    # Skip duplicates for the second element
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    # Skip duplicates for the third element
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif total>0:
                    r-=1
                else:
                    l+=1
        return result




"""
🌍 Real World Utility: Where is 3Sum used?
The "3Sum" problem is a variation of the Subset Sum Problem, which is critical in fields requiring reconciliation and combination verification.

1. Financial Fraud Detection (Wash Trading)
Use Case: Detecting "Zero-Sum" cycles.

How it works: Bad actors sometimes create loops of transactions to artificially inflate volume or launder money without changing their net balance (e.g., A pays B, B pays C, C pays A).

Application: Financial systems run 3Sum-like algorithms on transaction logs to identify sets of three (or more) transactions that net strictly to zero, flagging them for audit as potential wash trades.

2. Supply Chain Logistics (Container Loading)
Use Case: Optimizing weight distribution (Bin Packing variation).

How it works: Shipping containers often have strict weight limits or balance requirements.

Application: If a container has a remaining weight capacity of X and needs to be perfectly filled to prevent shifting, logistics software might search for 3 specific packages from the warehouse whose combined weight exactly equals X (or sums to 0 difference from target).
"""
