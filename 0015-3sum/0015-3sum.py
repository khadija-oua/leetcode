class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        R=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            T=-nums[i]
            r=len(nums)-1
            l=i+1
            while l < r:
                x= nums[l] + nums[r]
                if x > T:
                    r-=1
                elif x ==T:
                    R.append([nums[i],nums[r],nums[l]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:l+=1
        return R