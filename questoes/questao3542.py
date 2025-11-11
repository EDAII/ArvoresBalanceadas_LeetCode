from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def helper(l, r, base):
            if l > r:
                return 0
            
            min_val = min(nums[l:r+1])
            ops = min_val - base
            
            i = l
            while i <= r:
                if nums[i] == min_val:
                    i += 1
                else:
                    j = i
                    while j <= r and nums[j] > min_val:
                        j += 1
                    ops += helper(i, j-1, min_val)
                    i = j
            return min(ops, r-l+1)  
        
        return helper(0, len(nums)-1, 0)
