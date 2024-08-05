class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr=[1]*(n+1)
        i2=i3=i5=1
        for i in range(2,n+1):
            i2ugly=arr[i2]*2        
            i3ugly=arr[i3]*3     
            i5ugly=arr[i5]*5
            minugly=min(i2ugly,i3ugly,i5ugly)
            arr[i]=minugly
            if minugly==i2ugly:
                i2+=1
            if minugly==i3ugly:
                i3+=1
            if minugly==i5ugly:
                i5+=1
        return arr[n]      
