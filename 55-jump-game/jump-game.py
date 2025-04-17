class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx=0
        for i in range(len(nums)):
            if i>maxidx:
                return False
            maxidx=max(maxidx,nums[i]+i)
        return True
