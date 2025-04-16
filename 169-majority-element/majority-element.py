class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=list(set(nums))
        m=0
        ele=None
        for i in a:
            if m<nums.count(i):
                m=nums.count(i)
                ele=i
        return ele