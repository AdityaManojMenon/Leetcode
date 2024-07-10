class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        if len(arr) == 0:
            return 0

        max_len = 1
        curr_max = 1

        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                if (arr[i] > arr[i-1] and (i == 1 or arr[i-1] < arr[i-2])) or (arr[i] < arr[i-1] and (i == 1 or arr[i-1] > arr[i-2])):
                    curr_max += 1
                else:
                    curr_max = 2
            else:
                curr_max = 1
            max_len = max(max_len, curr_max)

        return max_len

        
                    
                
            
                
            
            
        
        