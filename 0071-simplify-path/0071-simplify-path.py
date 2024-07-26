class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split('/')
        stack=[]
        for i in a:
            if len(i)==0 or i=='.':
                continue
            elif i=='..':
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append('/'+i)
        res= "".join(stack) 
        if res=='':
            return '/'
        else:    
            return res