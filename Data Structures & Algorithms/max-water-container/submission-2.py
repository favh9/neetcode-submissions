class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        """ Translate
        The problem asks us to figure out the maximum amount of water that can be stored
        in between 2 or more bars.
        
        """

        """ Requirements
        We are given a list of integers with the heights of all of these bars.
        To solve the question, we must output the max area.
        We can assume that there will be at least 2 bars and the height of each bar is >= 0.
        """

        """ Approach
        Using 2 pointers, we can find the area between two bars.
        The area between two bars is the width x min(height1, height2)
        The maximum area is updated every time we find a value > than the last.
        """

        """ Code / Pseudocode
        maxArea = 0
        1 pointer at the start and another at the end
        calculate area =  (left-right) * min(height1,height2)
        if area > maxArea, update maxArea to area
        move the smallest pointer (left or right), if they're equal, move the right
        stop when left == right
        return maxArea
        """

        left = 0
        right = len(heights)-1
        maxArea = 0

        while left != right:
            area = (right-left) * min(heights[left], heights[right])

            if area > maxArea:
                maxArea = area
            
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea













