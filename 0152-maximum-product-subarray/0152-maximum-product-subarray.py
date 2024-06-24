class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = max_product = min_product = nums[0]
        
        for num in nums[1:]:
            
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, max_product*num)
            min_product = min(num, min_product*num)
            
            res =  max(res,max_product)
        return res
        