"""
PROBLEM STATEMENT:
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
"""

"""
SOLUTION APPROACH: Prefix and Suffix Product Arrays
* Precomputation: The solution uses two auxiliary arrays, 'pre' and 'suff', to 
  store products of elements before and after each index.
* Prefix Calculation: The 'pre' array is filled by multiplying the current 
  prefix product with the previous element in the input list.
* Suffix Calculation: Simultaneously, the 'suff' array is filled from right to 
  left, storing the cumulative product of elements to the right of each index.
* Result Construction: A final pass multiplies the prefix and suffix values 
  at each index to get the product of all elements except 'nums[i]'.



Complexity Analysis:
- Time Complexity: O(n)
  The code performs two linear passes (one for filling pre/suff and one for the result).
- Space Complexity: O(n)
  The solution uses O(n) extra space for the prefix and suffix arrays.

Optimal Complexity:
- Time: O(n)
- Space: O(1) (excluding the output array, by calculating suffix products on the fly).
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums=len(nums)
        pre = [1]*len_nums
        suff = [1]*len_nums
        prod = [1]*len_nums
        for i in range(1,len_nums):
            pre[i]=nums[i-1]*pre[i-1]
            suff[len_nums-1-i]=nums[len_nums-i]*suff[len_nums-i]
        
        for i in range(len_nums):
            prod[i] = pre[i]*suff[i]
        return prod

"""
REAL-WORLD APPLICATION:
The "Product of Array Except Self" logic mimics patterns found in systems 
that require cumulative data excluding a specific target:

1. Financial Systems & Risk Management:
   Used in calculating the impact of a single asset's removal from a portfolio. 
   By precalculating "prefix" and "suffix" risk values, analysts can quickly 
   determine the "what-if" scenario for any specific stock without re-scanning 
   the entire portfolio.

2. Digital Image Processing (Box Blurs):
   Similar logic is applied in 2D image filters where a pixel's value is 
   determined by its neighbors. Prefix sums (or products) help calculate 
   rectangular area sums in constant time after an initial linear pass.

3. Distributed Systems & Load Balancing:
   Calculating the relative weight or capacity of a node relative to the 
   rest of the cluster. If one node fails, the system uses pre-computed 
   aggregate stats to redistribute tasks.

4. Compiler Optimization:
   Used in data-flow analysis to determine the properties of variables 
   at a specific point in the code by aggregating information from all 
   preceding and succeeding blocks.
"""