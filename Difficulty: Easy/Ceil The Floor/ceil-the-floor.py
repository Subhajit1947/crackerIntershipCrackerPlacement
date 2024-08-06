#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        mini=[]
        maxi=[]
        for i in range(len(arr)):
            if arr[i]>=x:
                maxi.append(arr[i])
            if arr[i]<=x:
                mini.append(arr[i])
        return max(mini) if mini else -1,min(maxi) if maxi else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])


if __name__ == "__main__":
    main()

# } Driver Code Ends