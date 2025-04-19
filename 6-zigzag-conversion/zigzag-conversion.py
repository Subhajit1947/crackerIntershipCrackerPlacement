class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ans=''
        for i in range(numRows):
            idx=i
            idx_south=2*(numRows-i-1)
            idx_north=2*i
            going_south=True
            while idx<len(s):
                ans+=s[idx]
                if i==0:
                    idx+=idx_south
                elif i==numRows-1:
                    idx+=idx_north
                else:
                    if going_south:
                        idx+=idx_south
                    else:
                        idx+=idx_north
                    going_south=not going_south
        return ans