class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=0
        a,b=a[::-1],b[::-1]
        res=''
        for i in range(max(len(a),len(b))):
            digita=int(a[i]) if i<len(a) else 0
            digitb=int(b[i]) if i<len(b) else 0
            total=digita+digitb+c
            res=str(total%2)+res
            c=total//2
        if c==1:
            res='1'+res
        return res

