class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mincost=p[0]
        profit=0
        for i in range(1,len(p)):
            subprofit=p[i]-mincost
            profit=max(profit,subprofit)
            mincost=min(mincost,p[i])
        return profit