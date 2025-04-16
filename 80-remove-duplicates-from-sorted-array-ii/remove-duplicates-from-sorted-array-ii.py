class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if a.count(i)<2:
                a.append(i)
        for i in range(len(a)):
            nums[i]=a[i]
        return len(a)
