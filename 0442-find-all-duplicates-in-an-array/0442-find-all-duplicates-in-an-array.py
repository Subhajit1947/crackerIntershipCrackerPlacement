class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            ind=abs(nums[i])-1
            if nums[ind]<0:
                arr.append(ind+1)
            else:
                nums[ind]*=-1
        return arr
        