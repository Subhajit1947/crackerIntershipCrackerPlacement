#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def merge(self,arr,l,m,r):
        res=[]
        i=l
        j=m+1
        while i<m+1 and j<r+1:
            if arr[i]<=arr[j]:
               res.append(arr[i])
               i+=1
            else:
                res.append(arr[j])
                j+=1
        while i<m+1:
            res.append(arr[i])
            i+=1
        while j<r+1:
            res.append(arr[j])
            j+=1
        for ele in range(l,r+1):
            arr[ele]=res[ele-l]
        
        
    def mergeSort(self,arr, l, r):
        if l<r:
            m=(l+r)//2
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            self.merge(arr,l,m,r)


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends