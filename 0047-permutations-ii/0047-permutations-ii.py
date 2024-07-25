class Solution:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        d={i:0 for i in arr}
        for i in arr:
            d[i]+=1
        def dfs():
            if len(perm)==len(arr):
                res.append(perm.copy())
                return
            for i in d:
                if d[i]>0:
                    perm.append(i)
                    d[i]-=1
                    dfs()
                    perm.pop()
                    d[i]+=1
        dfs()
        return res