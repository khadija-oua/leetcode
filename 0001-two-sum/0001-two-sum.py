class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in range(len(nums)):
            x = target-nums[i]
            if x in m:
                return [i,m[x]]
            m[nums[i]]=i