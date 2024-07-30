class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        t11=[]
        for i in s:
            if i!='#':
                stack.append(i)
            else:
                if len(stack)>0:
                    stack.pop()
        for j in t:
            if j!='#':
                t11.append(j)
            else:
                if len(t11)>0:
                    t11.pop()
        print(stack,t11)
        if stack==t11:
            return True
        return False
            