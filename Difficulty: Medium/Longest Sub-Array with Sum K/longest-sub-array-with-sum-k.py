#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        d={0:-1}
        sum11=0
        c=0
        for i in range(len(arr)):
            sum11+=arr[i]
            if sum11-k in d.keys():
                c=max(c,i-d[sum11-k])
            if sum11 in d.keys():
                pass
            else:
                d[sum11]=i
        return c
                
      
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends