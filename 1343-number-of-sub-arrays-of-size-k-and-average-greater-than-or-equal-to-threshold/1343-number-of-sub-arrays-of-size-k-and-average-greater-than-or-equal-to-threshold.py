class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = 0
        window = sum(arr[:k])
        if window/k >= threshold:
            res+=1
        
        for i in range(k,len(arr)):
            window += arr[i]-arr[i-k]
            if window/k >= threshold:
                res+=1
        return res
                
            
            
        