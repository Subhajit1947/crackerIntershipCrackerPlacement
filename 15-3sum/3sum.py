class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        ans=[]
        a1={}
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    if f'{nums[i]}{nums[j]}{nums[k]}' not in a1.keys():
                        a1[f'{nums[i]}{nums[j]}{nums[k]}']=0
                        ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
                
            i+=1
        return ans
