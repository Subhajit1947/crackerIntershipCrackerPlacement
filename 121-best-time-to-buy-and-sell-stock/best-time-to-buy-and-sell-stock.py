class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mincost=prices[0]
        profit=0
        for i in range(1,len(prices)):
            profit11=prices[i]-mincost
            profit=max(profit,profit11)
            mincost=min(mincost,prices[i])
        return profit
        