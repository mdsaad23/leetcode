"""
PROBLEM STATEMENT: 56. Merge Intervals
---------------------------------------------------------
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# USER SOLUTION ANALYSIS
# ---------------------------------------------------------
# Solution Approach:
# • Sorting: The user sorts the input intervals based on the starting value. This is a crucial 
#   prerequisite for the greedy merging strategy.
# • Linear Scan: The code iterates through the sorted list once, maintaining a 'prev' interval.
# • In-place Modification: The code updates the end time of the 'prev' interval if an overlap is found.
# • Conditional Merging: If the current interval's start is less than or equal to the previous 
#   interval's end, they are merged. Otherwise, the previous interval is finalized.
#
# Time Complexity: O(n log n) due to the sorting step, where n is the number of intervals.
# Space Complexity: O(n) or O(log n) depending on the sorting implementation's auxiliary space.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        fin = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=prev[1]:
                prev[1]=max(prev[1],intervals[i][1])
            else:
                fin.append(prev)
                prev=intervals[i]
        fin.append(prev)
        return fin

# OPTIMAL SOLUTION ANALYSIS
# ---------------------------------------------------------
# Optimal Approach:
# • The user's approach is already near-optimal in terms of complexity.
# • Refinement: Instead of maintaining a separate 'prev' variable, we can use the 
#   last element of the result list (merged) to check for overlaps. This makes the code
#   cleaner and handles the edge case of an empty input more gracefully.
#
# Optimal Time Complexity: O(n log n)
# Optimal Space Complexity: O(n) to store the merged intervals.

class OptimalSolution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty or if the current 
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap, so we merge the current 
                # and previous intervals by updating the end time.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

"""
REAL-WORLD APPLICATION
---------------------------------------------------------
The logic used in merging intervals is fundamental to resource scheduling and 
time-series data management.

1. Calendar Systems:
   In applications like Google Calendar or Outlook, this algorithm is used to 
   calculate "busy time" slots. If a user has multiple overlapping meetings, 
   the system merges them to show a continuous block of unavailability to others.

2. Operating Systems (Memory Management):
   OS kernels manage free memory blocks using 'Free Lists'. When memory is 
   deallocated, the OS checks if the newly freed block is adjacent to existing 
   free blocks and merges them (coalescing) to prevent memory fragmentation.

3. Video Editing & Streaming:
   When rendering video or processing subtitles, multiple overlapping effect 
   layers or timestamped metadata need to be merged to determine the final 
   state of a specific frame or segment.

4. Database Indexing:
   In distributed databases, range queries often involve fetching data from 
   multiple partitions. Merging overlapping ranges reduces the number of 
   individual I/O operations required to fetch the requested dataset.
"""