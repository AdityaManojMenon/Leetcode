class Solution:
    def reverse(self, x: int) -> int:
        
        is_negative = x < 0
        
        x = abs(x)
        x = str(x)
        x = int(x[::-1])
        
        if is_negative:
            x = x*(-1)
        
        if(x < -2**31 or x > 2**31 - 1):
            return 0
        else:
            return x
        