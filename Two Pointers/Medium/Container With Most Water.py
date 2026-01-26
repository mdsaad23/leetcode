"""
PROBLEM DESCRIPTION:
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The max area is between index 1 (height 8) and index 8 (height 7). 
Width = 8 - 1 = 7. Height = min(8, 7) = 7. Area = 7 * 7 = 49.
"""

"""
SOLUTION APPROACH:
Two-Pointer Greedy Approach - O(N) Time

1. The problem asks us to maximize Area = Width * Height.
   - Width is the distance between indices (j - i).
   - Height is limited by the shorter of the two lines: min(height[i], height[j]).

2. Initialization:
   - Place one pointer 'i' at the beginning (0) and 'j' at the end (len-1). 
   - This gives us the maximum possible width to start.

3. The Greedy Choice (Crucial Step):
   - Calculate the area for the current pair and update 'max_area'.
   - To try and find a larger area, we must move our pointers inward.
   - WHICH pointer do we move?
     - If we move the TALLER line, the width decreases, and the height is still limited 
       by the SHORTER line (or becomes even smaller). The area can ONLY shrink.
     - Therefore, we *must* move the SHORTER line. By discarding the shorter line, 
       we hope to find a taller line that compensates for the loss in width.

4. Loop until the pointers meet.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        max_area = 0
        while i<j:
            # Calculate current area: Width (j-i) * Limited Height
            max_area= max(max_area,(j-i)*min(height[j],height[i]))
            
            # Greedy Logic: Always move the pointer of the shorter line
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return max_area