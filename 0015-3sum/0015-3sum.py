class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res=[]
        for index, val in enumerate(nums):
            if index>0 and val == nums[index-1]:
                continue
            left= index+1
            right= n-1 
            while left < right : 
                currentsum = val + nums[left]+ nums[right]
                if currentsum < 0:
                    left +=1
                elif currentsum >0:
                    right -=1
                else :
                    res.append([val,nums[left],nums[right]])
                    left+=1 
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    
        return res
                


        