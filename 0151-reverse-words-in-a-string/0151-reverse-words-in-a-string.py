class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(' ')
        ans=[]
        for i in range(len(a)-1,-1,-1):
            if a[i]!='':
                ans.append(a[i])
        s=''
        for i in range(len(ans)):
            if i!=len(ans)-1:
                s+=ans[i]+' '
            else:
                s+=ans[i]
        return s
