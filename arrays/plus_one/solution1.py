class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert list of ints into list of strings
        str_ints = [str(num) for num in digits]
        
        # combine into a single integer and increment
        n = int("".join(str_ints))
        n += 1
        
        # split into a list of integers
        res = [int(num) for num in str(n)]
        return res
        