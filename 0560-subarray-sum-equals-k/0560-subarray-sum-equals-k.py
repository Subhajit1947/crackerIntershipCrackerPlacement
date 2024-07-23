class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        sum1=0
        count=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1-k in d.keys():
                count+=d[sum1-k]
            if sum1 in d.keys():
                d[sum1]+=1
            else:
                d[sum1]=1
        return count


            
            
            