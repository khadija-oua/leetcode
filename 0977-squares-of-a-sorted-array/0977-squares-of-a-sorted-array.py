class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        s = deque()
        l,r = 0, len(nums)-1
        while l<=r:
            left, right = nums[l],nums[r]
            if abs(left)>=abs(right):
                s.appendleft(left**2)
                l+=1
            else : 
                s.appendleft(right**2)
                r-=1
        return list(s) 