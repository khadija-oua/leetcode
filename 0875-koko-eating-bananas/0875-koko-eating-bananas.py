class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k,piles):
            x=0
            for i in piles:
                x+=math.ceil(i / k)  
            return x
        low = 1
        high =max(piles)
        k=0
        x=0
        while (low <= high ):
            mid= low + (high-low)//2 
            x = helper(mid,piles)
            if x <= h :
                 high = mid -1
            else : low = mid + 1
        return low
