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

class Solution(object):
    
    # -----------------------------------------------------------
    # APPROACH 1: Optimized Brute Force (Your Original Solution)
    # -----------------------------------------------------------
    """
    SOLUTION APPROACH 1:
    Optimized Brute Force - O(N^2) Time
    
    1. Outer Loop: Iterate through the array with index 'i' to select the first number.
    2. Optimization (Neighbors): Check if neighbors sum to target immediately.
    3. Optimization (Duplicates): Skip duplicate 'i' values to avoid redundant work.
    4. Inner Loop: Iterate through 'j' from 'i+1'.
    5. Pruning: Since the array is sorted, break the inner loop if sum > target.
    """
    def twoSum_Approach1(self, numbers, target):
        for i in range(len(numbers)-1):
            if numbers[i]+numbers[i+1]==target:
                return [i+1,i+2]
            elif numbers[i]==numbers[i+1]:
                continue
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]>target:
                    break
                elif numbers[i]+numbers[j]==target:
                    return [i+1,j+1]

    # -----------------------------------------------------------
    # APPROACH 2: Two-Pointer Convergence (Optimal)
    # -----------------------------------------------------------
    """
    SOLUTION APPROACH 2:
    Two-Pointer Convergence - O(N) Time
    
    1. Initialize two pointers: 'left' at start (0) and 'right' at end (len-1).
    2. Loop while 'left' < 'right':
       - Calculate sum = numbers[left] + numbers[right].
       - If sum == target: We found the pair. Return 1-based indices.
       - If sum > target: The sum is too big. We must pick a smaller number, 
         so move 'right' pointer down (decrement).
       - If sum < target: The sum is too small. We must pick a larger number, 
         so move 'left' pointer up (increment).
    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1