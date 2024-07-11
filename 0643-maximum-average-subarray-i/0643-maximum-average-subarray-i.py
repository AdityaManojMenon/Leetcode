class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #find max sum window and then when returning divide the max sum window with k
        
        total = sum(nums[:k]) #initializing total to be of the first window
        max_sum = total
        
        for i in range(k,len(nums)):
            total += nums[i] - nums[i-k] #adding to the front of the window and removing from the back
            max_sum = max(max_sum,total)
        
        return max_sum/k
        
        
        