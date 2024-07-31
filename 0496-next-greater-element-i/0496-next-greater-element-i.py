class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d={n:i for i,n in enumerate(nums1)}
        # d={}
        # res=[-1]*len(nums1)
        # stack=[]
        # for i in range(len(nums2)):
        #     if nums2[i] not in d:
        #         continue
        #     else:
        #         for j in range(i+1,len(nums2)):
        #             if nums2[i]<nums2[j]:
        #                 res[d[nums2[i]]]=nums2[j]
        #                 break
        numToNextGreater = {}
        stack = []  

        for num in nums2:
            while stack and stack[-1] < num:
                numToNextGreater[stack.pop()] = num
            stack.append(num)

        return [numToNextGreater.get(num, -1) for num in nums1]