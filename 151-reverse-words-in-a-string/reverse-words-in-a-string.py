class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        a=[i for i in s.split(' ') if i!='']
        a=a[::-1]
        ans=''
        for i in range(len(a)-1):
            ans+=a[i]+' '
        ans+=a[-1]
        return ans