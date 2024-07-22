#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        a=sorted(A)
        minele=1000000000
        for i in range(M-1,N):
            mc=a[i]-a[i-M+1]
            minele=min(minele,mc)
        return minele


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends