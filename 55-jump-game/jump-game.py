class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx=0
        for i in range(len(nums)):
            if maxidx<i:
                return False
            maxidx=max(maxidx,i+nums[i])
        return True