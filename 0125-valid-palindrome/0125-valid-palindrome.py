class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        word = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                word+=char
        reverse = word[::-1]
        return word == reverse