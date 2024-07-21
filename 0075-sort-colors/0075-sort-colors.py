class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=set(nums)
        d={}
        for i in a:
            d[i]=nums.count(i)
        # b=[-1 for i in range(len(nums))]
        s=0
        for i in d:
            for j in range(s,s+d[i]):
                nums[j]=i
            s+=d[i]
        
        