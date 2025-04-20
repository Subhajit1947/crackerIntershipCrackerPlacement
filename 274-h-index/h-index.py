class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr=[0]*(len(citations)+1)
        for i in range(len(citations)):
            if citations[i]>=len(citations):
                arr[len(citations)]+=1
            else:
                arr[citations[i]]+=1
        count=0
        for i in range(len(arr)-1,-1,-1):
            count+=arr[i]
            if i<=count:
                return i
        
