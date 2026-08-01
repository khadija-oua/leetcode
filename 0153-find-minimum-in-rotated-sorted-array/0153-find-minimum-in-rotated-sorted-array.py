class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if  len(nums)==1 : return nums[0]
        if nums[low] < nums [high] : return nums[0] 
    
        while (low <= high):
            mid = low + (high - low )//2 
            if nums[mid]<nums[high] :
                if nums[mid]<nums[mid-1]: 
                    return nums[mid]
                else:high = mid-1 
            elif nums[mid]>nums[high] : 
                if nums[mid]>nums[mid+1]: 
                    return nums[mid+1]
                else: low = mid+1 
            