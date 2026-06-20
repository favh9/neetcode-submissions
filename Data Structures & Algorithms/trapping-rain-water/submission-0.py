class Solution:

    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        # prefix_max, the largest height to the left of i
        prefix_max = [0] * len(height)
        largest = height[0]
        for i in range(1, len(height)):
            
            prefix_max[i] = largest 
            if largest < height[i]:
                largest = height[i]

        # suffix_max, the largest height to the right of i
        suffix_max = [0] * len(height)
        largest = height[len(height)-1]
        for i in range(len(height)-1, -1, -1):
            
            suffix_max[i] = largest 
            if largest < height[i]:
                largest = height[i]

        area = 0
        for i in range(len(height)):
            
            bucket = min(prefix_max[i], suffix_max[i]) - height[i]

            if bucket < 0:
                area += 0
            else:
                area += bucket
            
        return area
            
            









        