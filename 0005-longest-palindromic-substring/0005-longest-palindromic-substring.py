class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        
        for i in range(len(s)):
            #odd 
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]: #checking plaindrom from the middle of string
                if r-l+1 > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                l-=1
                r+=1
            #even
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]: #checking plaindrom from the middle of string
                if r-l+1 > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                l-=1
                r+=1
                
        return res
        