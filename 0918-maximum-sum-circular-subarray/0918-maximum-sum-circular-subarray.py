class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def kadane(arr):
            max_sum = float('-inf')
            curr_sum = 0
            for num in arr:
                curr_sum += num
                max_sum = max(max_sum, curr_sum)
                if curr_sum < 0:
                    curr_sum = 0
            return max_sum 
        
        max_kadane = kadane(nums) # max for the straight array
        
        #we can find the min to subarray and subtract from total to find max in circular subarray
        
        inverted_nums = [-num for num in nums]
        max_inverted = kadane(inverted_nums)
        min_inverted = -max_inverted
        
        total = sum(nums)
        
        max_circular = total - min_inverted
        
        if max_circular == 0:
            return max_kadane
        
        return max(max_kadane,max_circular)
        
      
        
        
                    
                
        
        
                
        
        
        
       
            
        