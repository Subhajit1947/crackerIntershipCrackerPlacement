#User function Template for python3

class Solution:
	def binary_to_decimal(self, s):
        s11=s[::-1]
		de=0
		for i in range(len(s11)):
		    de+=int(s11[i])*(2**i)
		return de


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution();
		ans = ob.binary_to_decimal(str)
		print(ans)
# } Driver Code Ends