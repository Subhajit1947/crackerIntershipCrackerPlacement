class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        ans=''
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                ans+=s[i]
                i+=1
                j+=1
            else:
                j+=1
        if ans==s:
            return True
        else:
            return False
