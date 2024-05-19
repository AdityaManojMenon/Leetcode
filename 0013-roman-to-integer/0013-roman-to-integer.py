class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        for i in range(len(s)):

            if(s[i] == 'I'):
                total+=1

            if((i == 0 and s[i] == 'V') or (s[i] == 'V' and s[i-1] !='I')):
                total+=5
            if(i != 0 and s[i] == 'V' and s[i-1] == 'I'):
                total+=3
            
            if((i == 0 and s[i] == 'X') or (s[i] == 'X' and s[i-1] !='I')):
                total+=10
            if(i != 0 and s[i] == 'X' and s[i-1] == 'I'):
                total+=8

            if((i == 0 and s[i] == 'L') or (s[i] == 'L' and s[i-1] !='X')):
                total+=50
            if(i != 0 and s[i] == 'L' and s[i-1] == 'X'):
                total+=30

            if((i == 0 and s[i] == 'C') or (s[i] == 'C' and s[i-1] !='X')):
                total+=100
            if(i != 0 and s[i] == 'C' and s[i-1] == 'X'):
                total+=80
            
            if((i == 0 and s[i] == 'D') or (s[i] == 'D' and s[i-1] !='C')):
                total+=500
            if(i != 0 and s[i] == 'D' and s[i-1] == 'C'):
                total+=300
            
            if((i == 0 and s[i] == 'M') or (s[i] == 'M' and s[i-1] !='C')):
                total+=1000
            if(i != 0 and s[i] == 'M' and s[i-1] == 'C'):
                total+=800
            
        return total
            
                