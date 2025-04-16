class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=[]
        j=0
        k=0
        for i in range(m+n):
            if j<m and k<n:
                if nums1[j]<=nums2[k]:
                    arr.append(nums1[j])
                    j+=1
                elif nums1[j]>nums2[k]:
                    arr.append(nums2[k])
                    k+=1
            elif j<m and k>=n:
                arr.append(nums1[j])
                j+=1
            elif j>=m and k<n:
                arr.append(nums2[k])
                k+=1
        for i in range(m+n):
            nums1[i]=arr[i]
        