class Solution(object):
    def search(self, nums, target):
        r = 0
        l= len(nums)-1

        while r<=l: 
            n= r + (l-r)//2
            if nums[n]==target : return n
            elif nums[n] > target : l=n-1 
            else :  r=n+1
        return -1