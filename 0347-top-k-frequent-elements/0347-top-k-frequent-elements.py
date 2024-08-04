class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        arr=[]
        for i in d:
            arr.append((i,d[i]))
        a11=sorted(arr,key=lambda x:x[1],reverse=True)
        print(a11)
        res=[]
        for i in range(k):
            res.append(a11[i][0])
        return res
