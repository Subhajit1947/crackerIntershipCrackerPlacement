class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        i=0
        while i<N:
            if arr[i]<=0 or arr[i]>N or arr[i]>P:
                i+=1
                continue
            temp=arr[i]-1
            if arr[temp]>0:
                arr[i]=arr[temp]
                arr[temp]=-1
            else:
                arr[temp]+=-1
                arr[i]=0
                i+=1
        for j in range(N):
            if arr[j]<0:
                arr[j]=-arr[j]
            else:
                arr[j]=0
                
                
            
            
        
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        P = int(input())
        ob = Solution()
        ob.frequencyCount(arr, N, P)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1

# } Driver Code Ends