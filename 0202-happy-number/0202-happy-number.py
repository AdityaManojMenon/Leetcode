class Solution:
    def isHappy(self, n: int) -> bool:
        
        tracker = []
        
        if n == 1:
            return True
        
        while n not in tracker:
            tracker.append(n)
            num = 0
            for i in str(n):
                num += int(i)**2
            n = num
            
            if n == 1:
                return True
        
        return False
                