#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        s=str(n)
        ans=0
        for i in s:
            ans+=int(i)**3
        if ans==n:
            return 'true'
        else:
            return 'false'

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends