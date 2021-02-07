class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            for i in range(idx+1, len(nums)):
                if num + nums[i] == target:
                    return [idx, i]
