class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=[]
        for i in nums:
            if i!=val:
                a.append(i)
        k=len(a)
        for i in range(k):
            nums[i]=a[i]
        return k