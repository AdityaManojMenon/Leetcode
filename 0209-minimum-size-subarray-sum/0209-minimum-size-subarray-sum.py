class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_lenght = float('inf')
        window = 0
        L = 0
        for R in range(len(nums)):
            window+=nums[R]
            while window >= target:
                min_lenght = min(min_lenght,R-L+1)
                window -= nums[L]
                L+=1
        if min_lenght == float('inf'):
            return 0
        else:
            return min_lenght
            
            
        