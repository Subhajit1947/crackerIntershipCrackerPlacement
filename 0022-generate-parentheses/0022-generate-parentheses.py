class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        temp=[]
        def backtrack(openn,closen):
            if openn==closen==n:
                res.append("".join(temp))
                return
            if openn<n:
                temp.append('(')
                backtrack(openn+1,closen)
                temp.pop()
            if closen<openn:
                temp.append(')')
                backtrack(openn,closen+1)
                temp.pop()
        backtrack(0,0)
        return res