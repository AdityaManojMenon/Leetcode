class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        num_map = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],
                   "6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"], "9":["w","x","y","z"]} 
        
        if not digits:
            return []
        res = []
        
        def backtrack(index,path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            possible_letters = num_map[digits[index]]
            
            for letter in possible_letters:
                backtrack(index+1, path + [letter])
                
        backtrack(0,[])
        return res
            
            
                    
        