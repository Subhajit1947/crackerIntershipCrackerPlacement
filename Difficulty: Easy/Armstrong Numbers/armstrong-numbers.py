#User function Template for python3

class Solution:
    def armstrongNumber (self, num):
        # code here 
        s=str(num)
        ans=0
        for i in s:
            ans+=int(i)**3
        if ans==num:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        flag = ob.armstrongNumber(n)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends