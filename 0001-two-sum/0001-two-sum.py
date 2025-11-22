class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x=target-nums[i]
            if x in nums and nums.index(x)!=i:
                return [i,nums.index(x)]