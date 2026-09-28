class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s= sorted(nums)
        d={}
        r=[]
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i 
        for i in range(len(nums)):
            r.append(d[nums[i]])
        return r
            

        