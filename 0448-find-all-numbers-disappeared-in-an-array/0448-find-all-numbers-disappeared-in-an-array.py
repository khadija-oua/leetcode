class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n= len(nums)
        s=set(nums)
        r=[]
        for i in range(1,n+1):
            if i not in s : r.append(i)
        return r
