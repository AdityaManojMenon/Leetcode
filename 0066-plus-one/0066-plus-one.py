class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        for i in digits:
            temp+=str(i)
        final_str = str(int(temp)+1)
        res = list(map(int,final_str))
        return res
        
        


        