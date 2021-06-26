class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_str = [char for char in list(s) if char.isalnum()]
        s = "".join(stripped_str)
        
        for i in range(len(s)//2):
            char1 = s[i].lower()
            char2 = s[len(s)-1-i].lower()
            if char1 != char2:
                return False
        return True