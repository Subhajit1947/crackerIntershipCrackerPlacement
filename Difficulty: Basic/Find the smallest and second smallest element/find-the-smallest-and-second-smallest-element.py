#User function Template for python3
class Solution:
    def minAnd2ndMin(self, arr):
        a=sorted(list(set(arr)))
        
        if len(a)<=1:
            return (-1,-1)
        if a[0]!=a[1]:
            return (a[0],a[1])
        else:
            return (-1,-1)
        
        
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        product = obj.minAnd2ndMin(arr)
        if product[0] == -1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends