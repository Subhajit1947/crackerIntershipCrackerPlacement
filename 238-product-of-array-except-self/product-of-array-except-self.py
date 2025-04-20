class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        suf=[1]
        ans=[]
        for i in nums[0:len(nums)-1]:
            pre.append(pre[-1]*i)
        for i in nums[len(nums)-1:0:-1]:
            suf.append(suf[-1]*i)
        suf=suf[::-1]
        for i in range(len(nums)):
            ans.append(pre[i]*suf[i])
        return ans