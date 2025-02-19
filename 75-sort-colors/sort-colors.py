class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={}
        a=set(nums)
        for i in a:
            d[i]=nums.count(i)
        ans=0
        for i in d:
            for j in range(0,d[i]):
                nums[ans]=i
                ans+=1

        