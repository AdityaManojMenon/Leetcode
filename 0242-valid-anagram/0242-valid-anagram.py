class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        checker_s = {}
        checker_t = {}
        
        for i in s:
            if i not in checker_s:
                checker_s[i] = 1
            else:
                checker_s[i] += 1
        
        for i in t:
            if i not in checker_t:
                checker_t[i] = 1
            else:
                checker_t[i] += 1
                
        if checker_t == checker_s:
            return True
        else:
            return False