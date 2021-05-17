# O(n) time, O(n) space
def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            match = target - nums[i]
            if match in num_map:
                return [num_map[match], i]
            else:
                num_map[nums[i]] = i
        return []