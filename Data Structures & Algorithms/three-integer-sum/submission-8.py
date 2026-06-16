class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """ Translate
        given a list of integers, find all triplets without repeating indices.
        """

        """ Requirements
        output the list of triplets
        """

        """ Approach
        modify the requirements such that nums[i] + nums[j] + nums[k] = 0 is instead:
            nums[j] + nums[k] = -nums[i]
            target = -nums[i]

        use 3 pointers; p1, p2, and p3
        sort the list
        we traverse the list to get a different target
        we find the target with the help of p2 and p3
        then return all triplets found
        """
        res = []
        nums.sort()
        p1 = 0
        p2 = 1
        p3 = len(nums) - 1

        while p1 < len(nums) - 2:
            p2 = p1 + 1
            p3 = len(nums) - 1

            while p2 < p3:
                
                s = nums[p1] + nums[p2] + nums[p3]

                if s == 0:
                    res.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1
                    p3 -= 1
                    while p2 < p3 and nums[p2-1] == nums[p2]:
                        p2 += 1
                    while p3 > p2 and nums[p3+1] == nums[p3]:
                        p3 -= 1
                elif s < 0:
                    p2 += 1
                else:
                    p3 -= 1
            p1 += 1
            while p1 < len(nums) - 2 and nums[p1-1] == nums[p1]:
                p1 += 1
            

        return res