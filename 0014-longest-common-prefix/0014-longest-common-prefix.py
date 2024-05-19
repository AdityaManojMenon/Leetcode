class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        length = len(res)
        for i in range(1, len(strs)):
            while strs[i].find(res):
                res = res[:length-1]
                length-=1
        return res


        