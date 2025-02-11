class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            a=str(x)[1::][::-1]
            if -int(a)<-2**31:
                return 0
            return -int(a)
        elif x>=0:
            a=str(x)[::-1]
            if int(a)>((2**31)-1):
                return 0
            return int(a)
        else:
            return 0