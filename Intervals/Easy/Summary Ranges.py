"""
PROBLEM STATEMENT:
You are given a sorted unique integer array 'nums'.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer 
x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Example:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

--------------------------------------------------------------------------------
SOLUTION APPROACH (USER'S IMPLEMENTATION):
* The user employs a 'Single Pass Linear Scan' approach with manual state tracking.
* Tracking Variables: 'start' marks the beginning of a potential range, 'prev' tracks 
  the immediate predecessor, and 'counter' acts as a flag to distinguish between 
  a single-element range and a multi-element range.
* Conditional Logic: The code uses nested if-else statements to check if the 
  current element (nums[i]) is consecutive to the previous one.
* Final Edge Case Handling: Since the loop finishes before processing the last 
  identified range, an additional check is performed outside the loop to append 
   the final range to the result array.

COMPLEXITY ANALYSIS:
* User Time Complexity: O(n) - The array is traversed exactly once.
* User Space Complexity: O(1) - Excluding the output list, only a constant amount 
  of extra space is used for variables (start, prev, counter).
* Optimal Time Complexity: O(n)
* Optimal Space Complexity: O(1) (excluding output list)

INEFFICIENCY NOTES:
Your solution is logically correct and achieves the optimal O(n) time complexity. 
However, it is 'syntactically inefficient.' The use of a 'counter' and nested 
if-else blocks makes the logic more complex than necessary. In "Interval" 
problems, the goal is often to identify the 'boundary' where the continuity 
breaks. By simplifying the loop to only look for the break points, you can 
reduce the number of variables and conditional checks.
--------------------------------------------------------------------------------
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arr = []
        if len(nums)>0:
            start = nums[0]
            prev=nums[0]
            counter =0
            for i in range(1,len(nums)):
                if counter==0:
                    if nums[i]==start+1:
                        counter+=1
                        prev=nums[i]
                    else:
                        arr.append(str(nums[i-1]))
                        start = nums[i]
                else:
                    if nums[i]==prev+1:
                        counter+=1
                        prev=nums[i]
                    else:
                        arr.append(str(start)+"->"+str(prev))
                        prev=nums[i]
                        start=nums[i]
                        counter=0
            if counter==0:
                arr.append(str(nums[-1]))
            else:
                arr.append(str(start)+"->"+str(prev))
            return arr
        else:
            return []

"""
OPTIMAL CODE (Cleaned Logic):
Below is a more Pythonic/Optimized way to write the same logic:

def summaryRanges(nums):
    ranges = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
        if start != nums[i]:
            ranges.append(str(start) + "->" + str(nums[i]))
        else:
            ranges.append(str(start))
        i += 1
    return ranges

--------------------------------------------------------------------------------
REAL-WORLD APPLICATION: "INTERVALS" AND DATA COMPRESSION

WHAT ARE INTERVALS?
In computer science, "Intervals" represent a range of values with a defined 
start and end. Problems in this category involve merging overlapping ranges, 
finding gaps between ranges, or, as seen here, 'compressing' individual points 
into continuous segments.

REAL-WORLD USAGE:
1. Data Compression (Run-Length Encoding):
   Similar to how this problem groups consecutive numbers, video and image 
   compression algorithms group identical or consecutive pixel values to 
   save space instead of storing every single data point.

2. Database Indexing & Memory Management:
   Operating systems manage RAM using 'Free Lists.' Instead of tracking every 
   single byte of free memory, the OS stores 'intervals' of memory addresses 
   (e.g., "Address 1000 to 5000 is free") to optimize lookup speed.

3. Calendar and Scheduling Systems:
   Applications like Google Calendar or Outlook use interval logic to detect 
   'conflicts' or to 'summarize' availability. For example, if you are busy 
   from 1 PM to 2 PM and 2 PM to 3 PM, the system summarizes your status 
   as "Busy from 1 PM -> 3 PM."
--------------------------------------------------------------------------------
"""