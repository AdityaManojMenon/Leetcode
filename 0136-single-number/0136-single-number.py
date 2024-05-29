class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict_ = {}
        
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        
        res = [x for x in dict_ if dict_[x] == 1]
        return res[0]
        