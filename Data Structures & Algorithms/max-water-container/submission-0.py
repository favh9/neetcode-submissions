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
         
        for r in range(1,len(heights)):
        
            for l in range(r-1, -1, -1):
                
                area = r - l * min(heights[l], heights[r])
                
                if maxArea < area:
                    maxArea = area
            
        return maxArea
        """

        maxArea = 0
        
        for r in range(1, len(heights)):
            
            l = r - 1

            while l >= 0:
                
                area = (r - l) * min(heights[l], heights[r])
                
                if maxArea < area:
                    maxArea = area
                
                l -= 1
            
        return maxArea


















