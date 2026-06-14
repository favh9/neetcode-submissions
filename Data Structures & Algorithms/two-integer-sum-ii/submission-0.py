class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        """ Requirements
        arr[index1] + arr[index2] == target
        index1 < index2
        output -> [index1, index2]

        Assume there is always exactly 1 solution
        indices are to be returned 1-indexed
        the array is in non-decreasing order
        """

        """ Approach
        Use 2 pointers, left and right directly on opposite ends of the list.
        If we need a smaller sum, we decrease the right pointer;
        if we need a larger sum, we increase the left pointer;
        we return the indices once the sum matches the target
        """ 

        """ Code / Pseudocode  
        instantiate l = 0 and r = len(numbers)-1

        while l < r
            sum = arr[l] + arr[r]
            if sum == target, return [l+1, r+1]
            elif sum == 0 and x is negative, 
                r--
            elif sum == 0 and x is positive,
                l++ 
            elif sum < x, # add
                l++
            elif sum > x, # subtract
                r++
            else
                return [-99999,99999] # error
        """

        l = 0
        r = len(numbers)-1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target: # target found
                return [l+1,r+1]
            elif sum == 0 and target < 0: # find a smaller sum
                r -= 1
            elif sum == 0 and target > 0: # find a larger sum
                l += 1
            elif sum < target: # find a larger sum
                l += 1
            elif sum > target: # find a smaller sum
                r -= 1
            else:
                return [-9999, 9999]    # error: target will never be found
            
        return [-9999, 9999] # target not found error









