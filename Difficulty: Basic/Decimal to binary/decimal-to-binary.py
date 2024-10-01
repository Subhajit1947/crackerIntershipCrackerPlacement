#User function Template for python3
def toBinary(n):
    s=''
    while n>0:
        m=n%2
        s=str(m)+s
        n=n//2
    print(s)
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    for _ in range(int(input())):
        n=int(input())
        toBinary(n)

    
# } Driver Code Ends