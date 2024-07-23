class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=sum(cardPoints[:k])
        rsum=0
        maxsum=lsum
        rindex=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            maxsum=max(maxsum,lsum+rsum)
            rindex-=1
        return maxsum