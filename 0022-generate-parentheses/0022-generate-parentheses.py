class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def validoutcomes(o,c,path): #o is open c is close
            if o == c == n:
                res.append(path)
                return
            if o < n:
                validoutcomes(o+1,c,path+"(")
            if c < o:
                validoutcomes(o,c+1,path+")")
            
        validoutcomes(0,0,"")
        return res
            
                    