#User function Template for python3
import math
class Solution:
    def isPrime (self, n):
        if n<1:
            return 0
        if n==1:
            return 0
        if n==2 or n==3:
            return 1
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
        print("~")
# } Driver Code Ends