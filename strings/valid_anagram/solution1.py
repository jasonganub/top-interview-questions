class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # store s into hashmap
        # loop through t and deduct from hashmap
        # loop through hashmap and if any val not 0, return true, else false
        
        if len(s) != len(t):
            return False
        
        charmap = {}
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            
            if char1 not in charmap:
                charmap[char1] = 1
            else:
                charmap[char1] += 1
            
            if char2 not in charmap:
                charmap[char2] = -1
            else:
                charmap[char2] -= 1
        
        for key in charmap:
            if charmap[key] != 0:
                return False
        
        return True