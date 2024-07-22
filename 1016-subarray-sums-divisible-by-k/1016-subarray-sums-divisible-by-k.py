class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        s=0
        count=0
        for i in range(len(nums)):
            s+=nums[i]
            r=s%k
            while r<0:
                r+=k
            if r not in d.keys():
                d[r]=1
            else:
                count+=d[r]
                d[r]+=1
        return count


