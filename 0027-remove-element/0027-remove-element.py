class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr=[]
        for i in nums:
            if i!=val:
                arr.append(i)
        for i in range(len(nums)):
            if i>=len(arr):
                nums[i]='_'
            else:
                nums[i]=arr[i]
        return len(arr)