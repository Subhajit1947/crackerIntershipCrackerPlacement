class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        cost=0
        i=0
        j=len(nums)-1
        while i<j:
            cost+=abs(nums[j]-nums[i])
            i+=1
            j-=1
        return cost