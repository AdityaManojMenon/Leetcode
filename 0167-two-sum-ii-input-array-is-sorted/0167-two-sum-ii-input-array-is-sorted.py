class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = 0
        R = len(nums)-1
        while L < R:
            if nums[L] + nums[R] == target:
                nums = [L+1,R+1]
                break
            if nums[L] + nums[R] > target:
                R-=1
            elif nums[L] + nums[R] < target:
                L+=1
        return nums
            
        