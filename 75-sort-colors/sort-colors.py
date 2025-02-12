class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={}
        a=set(nums)
        for i in a:
            d[i]=nums.count(i)
        s=0
        for i in d:
            for j in range(s,s+d[i]):
                nums[j]=i
            s+=d[i]
            
        