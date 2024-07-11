class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict_tracker = {}
        for i in range(len(nums)):
            if nums[i] in dict_tracker and i - dict_tracker[nums[i]]  <= k:
                return True
            dict_tracker[nums[i]] = i
        return False
                
        