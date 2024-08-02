class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0:1}
        res = 0
        curr_sum = 0
        for num in nums:
            curr_sum+=num
            diff = curr_sum - k
            res+=hash_map.get(diff,0)
            hash_map[curr_sum] = 1 + hash_map.get(curr_sum,0)
        return res
        
        