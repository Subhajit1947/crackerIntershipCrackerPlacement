class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def recurssion(arr,d):
            if len(arr)==len(nums):
                res.append(arr[:])
                return

            for i in range(len(nums)):
                if d[nums[i]]==False :
                    arr.append(nums[i])
                    d[nums[i]]=True
                    recurssion(arr,d)
                    arr.pop()
                    d[nums[i]]=False

        d={}
        for j in nums:
            d[j]=False
        recurssion([],d)
        return res
        