#User function Template for python3

class Solution:
    def lcmAndGcd(self, a, b):
        n1,n2=a,b
        while n1%n2!=0:
            rem=n1%n2
            n1=n2
            n2=rem
        gcd=n2
        lcm=(a*b)//gcd
        return lcm,gcd


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends