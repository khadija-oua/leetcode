class Solution(object):
    def maxProfit(self, prices):
        l=0
        p = 0
        for i in range (1,len(prices)):
            if prices[l]>prices[i-1] : l = i-1
            if prices[i]-prices[l] > p : p =prices[i]-prices[l]

        return p 