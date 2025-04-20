class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=list(set(nums))
        ele=-1
        c=0
        for i in a:
            if nums.count(i)>c:
                ele=i
                c=nums.count(i)
        return ele