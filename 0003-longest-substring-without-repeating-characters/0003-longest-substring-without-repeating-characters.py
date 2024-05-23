class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        char_set = set()
        max_length = 0
        start = 0
        end = 0
        
        while end < n:
            if s[end] not in char_set:
                char_set.add(s[end])
                end+=1
                max_length = max(max_length, end - start)
            else:
                char_set.remove(s[start])
                start+=1
                
        return max_length
                
            
                    