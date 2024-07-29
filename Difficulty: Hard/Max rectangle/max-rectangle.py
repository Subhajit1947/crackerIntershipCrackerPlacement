#User function Template for python3


class Solution:
    def maxarea(self,arr):
        maxa=0
        stack=[]
        for i,h in enumerate(arr):
            start=i
            while stack and stack[-1][-1]>h:
                index,height=stack.pop()
                maxa=max(maxa,height*(i-index))
                start=index
                
            stack.append((start,h))
        for i,h in stack:
            maxa=max(maxa,h*(len(arr)-i))
        return maxa
    def maxArea(self,M, n, m):
        arr=[0 for i in range(m)]
        res=0
        for i in range(n):
            for j in range(m):
                if M[i][j]==0:
                    arr[j]=0
                else:
                    arr[j]+=1
            res=max(res,self.maxarea(arr))
                   
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends