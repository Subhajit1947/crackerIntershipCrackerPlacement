class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zc=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zc.append(i)
        for i in zc:
            nums.append(0)
        print(nums,zc)
        for i in range(len(zc)):
            nums.pop(zc[i]-i)
        