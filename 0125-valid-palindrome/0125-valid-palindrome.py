class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #make all the characters in string lower
        s = s.lower()
        list1 = []
        
        #only add alpha characters to list1 in order
        for i in s:
            if i.isalpha() == True:
                list1.append(i)
            if i.isdigit() == True:
                list1.append(i)
                
        #List2 is list1 but reversed
        list2 = list1[::-1]
        
        #check if they are equal to each other
        
        if list1 == list2:
            return True
        else:
            return False
