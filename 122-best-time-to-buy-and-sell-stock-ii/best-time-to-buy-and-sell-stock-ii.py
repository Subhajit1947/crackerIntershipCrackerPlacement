class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def fn(idx,buy):
            if idx>=len(prices):
                return 0
            if (idx,buy) in dp.keys():
                return dp[(idx,buy)]
            else:
                if buy:
                    profit=max(-prices[idx]+fn(idx+1,0),fn(idx+1,1))
                else:
                    profit=max(prices[idx]+fn(idx+1,1),fn(idx+1,0))
                dp[(idx,buy)]=profit
                return profit
        return fn(0,1)