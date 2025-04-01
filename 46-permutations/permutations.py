class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def recurssion(arr,map1):
            if len(arr)==len(nums):
                ans.append(arr[:])
                return
            for i in range(len(nums)):
                if map1[i]==-1:
                    arr.append(nums[i])
                    map1[i]=1
                    recurssion(arr,map1)
                    a=arr.pop()
                    idx=nums.index(a)
                    map1[idx]=-1

        arr=[]
        map1=[-1]*len(nums)
        recurssion(arr,map1)
        return ans


