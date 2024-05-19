class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        word = ""
        for i in range(len(haystack)):
            word+=haystack[i]
            if needle in word:
                return i - len(needle) + 1
                break
        
        
        return -1
                
        