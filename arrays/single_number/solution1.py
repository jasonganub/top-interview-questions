class Solution:

    # O(n) time, O(1) space
    def singleNumber(self, nums: List[int]) -> int:
        num_map = {}
        for num in nums:
            if num in num_map:
                del num_map[num]
            else:
                num_map[num] = True
                
        
        for num in num_map:
            return num