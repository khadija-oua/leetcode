class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer=[0]*n
        prefix=[0]*n
        suffix=[0]*n

        prefix[0] = suffix[n-1] =1
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        for j in range (n-2,-1,-1):
            suffix[j]= suffix[j+1]*nums[j+1]
        for i in range (n):
            answer[i]=prefix[i]*suffix[i]
        return answer