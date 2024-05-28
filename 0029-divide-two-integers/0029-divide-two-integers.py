class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        #edge case:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        res_neg = (dividend < 0) != (divisor < 0) #checks if the answer is supposed to be negative or not

        dividend, divisor = abs(dividend), abs(divisor)

        res = 0

        while dividend >= divisor:
            temp,multiple = divisor,1
            while dividend >= temp+temp:
                temp += temp
                multiple += multiple
            dividend -= temp
            res += multiple

        if res_neg:
            res = -res
        else:
            res = res

        return max(-2**31,min(res,2**31))
            
        
                
            
            
            
        