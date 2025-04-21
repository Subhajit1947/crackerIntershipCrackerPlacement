class Solution:
    def isPalindrome(self, s: str) -> bool:
        s11=''
        for i in s:
            if (i>='a' and i<='z') or (i>='A' and i<='Z'):
                s11+=i.lower()
            elif i>='0' and i<='9':
                s11+=i
        print(s11)
        for i in range(len(s11)//2):
            if s11[i]!=s11[len(s11)-i-1]:
                return False
        return True