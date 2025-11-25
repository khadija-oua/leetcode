class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        S=0
        min=prices[0]
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            else:
                if prices[i]-min > S:
                    S= prices[i]-min 
        return S

      
        