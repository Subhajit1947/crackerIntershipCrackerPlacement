class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,
            'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000
        }
        i=0
        ans=0
        while i<len(s)-1:
            a=d[s[i]]
            b=d[s[i+1]]
            if a<b:
                ans+=d[s[i]+s[i+1]]
                i+=2
            else:
                ans+=d[s[i]]
                i+=1
        if i==len(s)-1:
            ans+=d[s[i]]
        return ans



        