class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ Approach / Observations
        Bruteforce - use a hash set and membership testing for sequence detections.
            Avg time - O(n^2) since we repeatedly search similar sequences
        Optimized - sort the list, increase count for every consecutive sequence, skip duplicates, otherwise reset count
        Best - use a hash set and membership testing to find a starting sequence (so num-1 is not in the set)
        """ 

        """ Pseudocode
        initialize hash set num_set
        add the numbers into the set # O(1) lookups
        initialize streak_max = 0 # to keep the longest streak count
        for every num in num_set # get the longest consecutive sequence
            initialize streak_count = 1
            if num-1 is not in num_set # we found the beginning of a sequence
                while num+1 is in num_set
                    streak_count++
                    num++
            if streak_count > streak_max
                streak_max = streak_count
        return streak_max
        """
        num_set = set(nums)
        streak_max = 0
        
        for num in num_set:
            streak_count = 1
            if num - 1 not in num_set:
                while num + streak_count in num_set:
                    streak_count += 1
            if streak_count > streak_max:
                streak_max = streak_count
                
        return streak_max
