#User function Template for python3

class Solution:
    def lcmAndGcd(self, a , b):
        # code here 
        if a==0 or b==0:
            return 0
        
        a11,b11=a,b
        while a%b!=0:
            a,b=b%a,a
        gcd=b
        hcf=(a11*b11)//gcd
        return hcf,gcd
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())

        ob = Solution()
        ptr = ob.lcmAndGcd(A, B)

        print(ptr[0], ptr[1])
        print("~")

# } Driver Code Ends