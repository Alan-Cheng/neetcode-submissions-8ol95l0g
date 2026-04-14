class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res not in h_map:
                h_map[nums[i]] = i
            else:
                return [h_map[res], i]
        
        return []