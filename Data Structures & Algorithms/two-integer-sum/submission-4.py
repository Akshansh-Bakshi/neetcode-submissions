class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        element_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in element_map:
                return [element_map[complement], i]

            element_map[nums[i]] = i