class Solution(object):
    def findMaxAverage(self, nums, k):
        a,b =0,k-1
        S=0
        for i in range (len(nums)):
            if i<b:
                S+=nums[i]
            elif i==b:
                S+=nums[i]
                best = float(S)/k
            else:
                S=S+nums[i]-nums[a]
                a+=1
                best=max(best,float(S)/k)
        return best
        