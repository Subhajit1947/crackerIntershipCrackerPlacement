class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=list(set(nums))
        d={}
        for i in a:
            d[i]=nums.count(i)
        for i in d:
            if d[i]>len(nums)//2:
                return i