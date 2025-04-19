class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        s=''
        a=min(strs,key=len)
        if a=='':
            return ''
        print(a)
        for i in range(len(a)):
            if all(a[i]==strs[j][i] for j in range(0,len(strs))):
                s+=a[i]
            else:
                break
                # if s!='':
                #     ans.append(s)
                # s=''
        if s!='':
            ans.append(s)
        print(ans)
        if len(ans)==0:
            return ''
        return max(ans,key=len)
