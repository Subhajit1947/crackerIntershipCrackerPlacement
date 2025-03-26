class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            if i==1:
                ans.append([1])
            elif i==2:
                ans.append([1,1])
            else:
                temp=[1]
                for j in range(len(ans[-1])-1):
                    temp.append(ans[-1][j]+ans[-1][j+1])
                temp.append(1)
                ans.append(temp)
        return ans