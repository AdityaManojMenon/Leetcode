# could be parantheses_count < 0 in line 10
class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_count = 0
        bracket_count = 0
        curly_count = 0
        last_open = [' ']
        for i in s:
            if i == '(':
                parantheses_count-=1
                last_open.append('(')
            if i == ')' and (last_open[-1] != '(' or parantheses_count > 0):
                return False
            if i == ')' and (last_open[-1] == '(' or parantheses_count < 0):
                parantheses_count+=1
                last_open.pop(-1)

            if i == '[':
                bracket_count-=1
                last_open.append('[')
            if i == ']' and (last_open[-1] != '[' or bracket_count > 0):
                return False
            if i == ']' and (last_open[-1] == '[' or bracket_count < 0):
                bracket_count+=1
                last_open.pop(-1)
            
            if i == '{':
                curly_count-=1
                last_open.append('{')
            if i == '}' and (last_open[-1] != '{' or curly_count > 0):
                return False
            if i == '}' and (last_open[-1] == '{' or curly_count < 0):
                curly_count+=1
                last_open.pop(-1)

        if(bracket_count != 0 or parantheses_count != 0 or curly_count!=0):
            return False
        else:
            return True

            

            
        