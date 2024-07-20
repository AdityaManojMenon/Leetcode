class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if s is None:
            return 0
        
        count_tracker = {}
        L = 0
        res = 0
        
        for R in range(len(s)):
            if s[R] not in count_tracker:
                count_tracker[s[R]] = 1
            else:
                count_tracker[s[R]] += 1
            if (R - L + 1) - max(count_tracker.values()) <=k:
                res = max(res, R - L + 1)
            else:
                count_tracker[s[L]]-=1
                L+=1
        return res
        
        
        