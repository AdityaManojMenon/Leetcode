class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        """
        nums = [x**2 for x in nums]
        nums.sort()
        return nums
        """
        ans = list(map(lambda x : x**2,nums))
        ans.sort()
        return ans
                
        
        