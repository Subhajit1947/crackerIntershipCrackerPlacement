class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cost=prices[i]-minp
            profit=max(cost,profit)
            minp=min(prices[i],minp)
        return profit
