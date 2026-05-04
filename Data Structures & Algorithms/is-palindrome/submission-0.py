class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1] 


