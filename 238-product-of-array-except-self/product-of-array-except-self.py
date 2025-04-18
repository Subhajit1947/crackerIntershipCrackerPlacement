class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        suf=[1]
        ans=[]
        for i in range(len(nums)-1):
            pre.append(pre[-1]*nums[i])
        for i in range(len(nums)-1,0,-1):
            suf.append(suf[-1]*nums[i])
        suf.reverse()
        for i in range(len(nums)):
            ans.append(pre[i]*suf[i])
        return ans
            