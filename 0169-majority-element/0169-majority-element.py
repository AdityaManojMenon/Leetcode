class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        
        dict_tracker = {}
        
        for i in nums:
            if i not in dict_tracker:
                dict_tracker[i] = 1
            else:
                dict_tracker[i]+=1
        
        for num,count in dict_tracker.items():
            if count > n:
                return num
        