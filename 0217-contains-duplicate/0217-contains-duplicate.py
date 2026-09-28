class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set(nums)
        if len(nums) == len(set(nums)): return False
        else: return True