class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def fn(arr,r11):
            if len(arr)==len(nums):
                ans.append(arr[:])
                return
            for i in range(len(nums)):
                if r11[i]==-1:
                    arr.append(nums[i])
                    r11[i]=1
                    fn(arr,r11)
                    r11[i]=-1
                    arr.pop()
        
        arr=[]
        r=[-1]*len(nums)
        fn(arr,r)
        return ans

                
                
        