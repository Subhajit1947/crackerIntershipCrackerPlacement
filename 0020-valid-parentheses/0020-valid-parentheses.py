class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={
            ')':'(','}':'{',']':'['
        }
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if len(stack)>0:
                    top=stack.pop()
                else:
                    return False
                if top!=d[i]:
                    return False

                    
        if len(stack)==0:
            return True
        else:
            return False