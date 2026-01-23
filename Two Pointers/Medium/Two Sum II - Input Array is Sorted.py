"""
PROBLEM DESCRIPTION:
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers 'numbers' that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific 'target' number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same 
element twice. Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
"""

"""
SOLUTION APPROACH:
This solution utilizes an Optimized Brute Force approach that leverages the sorted property of the array to reduce unnecessary checks (pruning).

1. Outer Loop: Iterate through the array with index 'i' to select the first number.
2. Immediate Checks:
   - Check the adjacent element (i+1). If they sum to 'target', return immediately.
   - Duplicate Handling: If numbers[i] is the same as the next number (and they didn't sum to target), 
     skip this iteration to avoid redundant work.
3. Inner Loop: Iterate through 'j' starting from 'i+1' to find the second number.
4. Early Exit (Pruning): Since the array is sorted, if numbers[i] + numbers[j] exceeds the 'target', 
   we break the inner loop immediately. Any subsequent numbers will also be too large.
5. Match: If the sum equals 'target', return the 1-based indices.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)-1):
            # Optimization 1: Check immediate neighbor first
            if numbers[i]+numbers[i+1]==target:
                return [i+1,i+2]
            # Optimization 2: Skip duplicates to speed up iteration
            elif numbers[i]==numbers[i+1]:
                continue
            
            for j in range(i+1,len(numbers)):
                # Optimization 3: Pruning - Stop if sum exceeds target (because array is sorted)
                if numbers[i]+numbers[j]>target:
                    break
                elif numbers[i]+numbers[j]==target:
                    return [i+1,j+1]