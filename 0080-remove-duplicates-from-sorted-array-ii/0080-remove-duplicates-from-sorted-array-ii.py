class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L,R = 0,1
        seen_once = False
        
        while R < len(nums):
            if nums[L] == nums[R] and seen_once == False:
                seen_once = True
                L+=1
                R+=1
            elif nums[L] == nums[R] and seen_once == True:
                nums.pop(R)
            else:
                L+=1
                R+=1
                seen_once = False
        return R
        